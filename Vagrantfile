MEMORY = 512
CORES = 1
CLIENT = "client"
SERVER = "server"

Vagrant.configure("2") do |config|

    config.vm.box = "ubuntu/focal64"

    config.vm.define SERVER do |cfg|
        cfg.vm.hostname = SERVER
        cfg.vm.provider "virtualbox" do |vbox|
            vbox.name = SERVER
            vbox.memory = MEMORY
            vbox.cpus = CORES
        end
        cfg.vm.network "private_network", ip: "192.168.56.50", hostname: true
        cfg.vm.provision "file", source: "./server.py", destination: "~/server.py"
        cfg.vm.provision "shell", inline: "chmod +x /home/vagrant/server.py"
    end

    config.vm.define CLIENT do |cfg|
        cfg.vm.hostname = CLIENT
        cfg.vm.provider "virtualbox" do |vbox|
            vbox.name = CLIENT
            vbox.memory = MEMORY
            vbox.cpus = CORES
        end
        cfg.vm.network "private_network", ip: "192.168.56.100"
        cfg.vm.provision "file", source: "./client.py", destination: "~/client.py"
        cfg.vm.provision "shell", inline: "chmod +x /home/vagrant/client.py"
    end
end