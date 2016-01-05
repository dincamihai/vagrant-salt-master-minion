Vagrant.configure("2") do |config|
  ## Choose your base box
  config.vm.box = "hashicorp/precise64"
  config.vm.hostname = "salt"

  ## For masterless, mount your salt file root
  config.vm.synced_folder "salt/roots/", "/srv/salt/"
  # config.vm.synced_folder "salt/master/master.d/", "/etc/salt/master.d"
  # config.vm.synced_folder "salt/minion/minion.d/", "/etc/salt/minion.d"

  ## Use all the defaults:
  config.vm.provision :salt do |salt|

    salt.install_master = true
    salt.minion_key = "salt/minion/minion.pem"
    salt.minion_pub = "salt/minion/minion.pub"
    salt.minion_config = "salt/minion/minion.conf"

    salt.master_key = "salt/master/master.pem"
    salt.master_pub = "salt/master/master.pub"
    salt.master_config = "salt/master/master.conf"

    salt.seed_master = {minion: salt.minion_pub}

    salt.run_highstate = true

    salt.verbose = true
    salt.bootstrap_options = "-F -c /tmp/"

  end
end
