
#Resource-1: Create bastion subnet
resource "azurerm_subnet" "bastionsubnet" {
  name                 = "${azurerm_virtual_network.vnet}-${var.bastion_subnet_name}"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = var.bastion_subnet_address
  }


#Resource-2: Create NSG 
resource "azurerm_network_security_group" "bastion_subnet_nsg" {
  name                = azurerm_subnet.bastionsubnet.name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  }

#Resource-3: Associate subnet and NSG
resource "azurerm_subnet_network_security_group_association" "bastion_subnet_nsg_association" {
  depends_on = [azurerm_network_security_rule.bastion_nsg_rule_inbound]
  subnet_id                 = azurerm_subnet.bastionsubnet.id
  network_security_group_id = azurerm_network_security_group.bastion_subnet_nsg.id
}

#Resource-4: Create NSG Rules
#Locals block for security rules
locals {
  db_inbound_ports_map = {
    "100" : "3306",
    "110" : "1433",
    "120" : "5432"
  }
}

##NSG Inbound rule for Db tier subnets
resource "azurerm_network_security_rule" "bastion_nsg_rule_inbound" {
  for_each = db_inbound_ports_map
  name                        = "Rule-Port-${each.value}"
  priority                    = each.key
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = each.value
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name         = azurerm_resource_group.rg.name
  network_security_group_name = azurerm_network_security_group.bastion_subnet_nsg.name
}

