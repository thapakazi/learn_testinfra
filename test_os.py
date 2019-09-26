import testinfra
from pprint import pprint

def test_os_release(host):
    os_release = host.file("/etc/os-release")
    pkg_name = "apache"
    if os_release.contains("CentOS"):
       pkg_name = "httpd"
    elif os_release.contains("Ubuntu"):
       pkg_name = "apache2"
    elif os_release.contains("Arch Linux"):
       pkg_name = "nginx"
    pprint(pkg_name)
    apache = host.package(pkg_name)
    assert apache.is_installed
