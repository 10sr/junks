Vagrant boxes
=============


Basic Setup
-----------

    boxname=centos6.5
    vagrant box add $boxname <box_url>
    mkdir vagrant-centos
    cd vagrant-centos
    vagrant init $boxname
    vagrant up



Porpose of this Repository
--------------------------

* Try Vagrant
* Try provisioning tools
  * puppet
  * chef
  * ansible
