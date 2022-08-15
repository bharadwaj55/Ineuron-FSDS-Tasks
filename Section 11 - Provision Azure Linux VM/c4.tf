
resource "azurerm_linux_virtual_machine" "mylinuxvm" {
  name                = "mylinuxvm-1"
  resource_group_name = azurerm_resource_group.my-rg.name
  location            = azurerm_resource_group.my-rg.location
  size                = "Standard_DS1_v2"
  admin_username      = "azureuser"
  network_interface_ids = [
    azurerm_network_interface.myvmnic.id,
  ]

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
    sku       = "86-gen2"
    version   = "latest"
  }

  locals {
  custom_data = <<CUSTOM_DATA
  #!/bin/bash
  echo "Execute your super awesome commands here!"
  CUSTOM_DATA
  }

  # Using filebase64 to encode script
  custom_data = filebase64("app-scripts/cloud-init-jenkins.txt")

  # Encode and pass you script
  #   custom_data = base64encode(local.custom_data)

}