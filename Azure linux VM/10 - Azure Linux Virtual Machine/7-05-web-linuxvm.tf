
# Locals block for custom data 
locals {
  webvm_custom_data = <<CUSTOM_DATA
  #!/bin/sh
sudo yum install wget git -y
sudo yum install java-11-openjdk -y
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key
sudo yum upgrade
sudo yum install jenkins -y
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl daemon-reload
  CUSTOM_DATA
}

# Resource-4: Linux VM

resource "azurerm_linux_virtual_machine" "web_linuxvm" {
  name                = "${local.resource_name_prefix}-web-linuxvm"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  size                = "Standard_DS1_v2"
  admin_username      = "azureuser"
  network_interface_ids = [azurerm_network_interface.web_linuxvm_nic.id]
  # You can have multiple network interfaces, this is a list item
  # In case of banking sites, in single vm, they may be multiple interfaces
  # such as management traffic going via management interface, 
  # such as production traffic going via production interface,
  # such as super secure traffic going via super secure traffic interface,

  admin_ssh_key {
    username   = "azureuser"
    public_key = file("${path.module}/ssh-keys/terraform-azure.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "RedHat"
    offer     = "RHEL"
    sku       = "83-gen2"
    version   = "latest"
  }
  custom_data = base64encode(local.webvm_custom_data)
}