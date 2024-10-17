resource "azurerm_network_interface" "test" {
  name                = "project-3-NIC"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip}"
  }
}

# Created image from packer
data "azurerm_image" "test" {
  name                = "vm-ubuntu-1804"
  resource_group_name = "${var.resource_group}"
}

resource "azurerm_linux_virtual_machine" "test" {
  name                  = "${var.name}"
  location              = "${var.location}"
  resource_group_name   = "${var.resource_group}"
  size                  = "Standard_B2s"
  admin_username        = "${var.admin_username}"
  admin_password        = "${var.admin_password}"
  disable_password_authentication = false
  source_image_id       = "${data.azurerm_image.test.id}"
  network_interface_ids = [azurerm_network_interface.test.id]
 
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
}