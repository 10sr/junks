Package
=======


makepkg
-------

1. Download PKGBUILD from <https://aur.archlinux.org/> or somewhere.
2. Install by `makepkg -si`



Prefs
=====


brightness
----------

[Backlight - ArchWiki](https://wiki.archlinux.org/index.php/Backlight)

* `$ cd /sys/class/backlight`
* なんか適当に探す。 `max_brightness` を見つつ `brightness` を設定。


        # echo 20 >/sys/class/backlight/acpi_video0/brightness


system
------


* sysstat


Startup
-------

[systemd FAQ - ArchWiki](https://wiki.archlinux.org/index.php/Systemd_FAQ#Q:_How_can_I_make_a_script_start_during_the_boot_process.3F)

次のようなファイルを作り、 `/etc/systemd/system/myrc.service` として保存

    [Unit]
    Description=My script
    
    [Service]
    ExecStart=/usr/local/bin/myrc.sh
    
    [Install]
    WantedBy=multi-user.target

Enable it.

    # systemctl enable myrc.service

Create script file and chmod +x.


acpi 周りの設定とか
-----------------

現状、 acpi に関わるのは `acpid`, `systemd-logind`, `laptop-mode-tools` がある？

フタを閉じるとサスペンドするのは `/etc/systemd/logind.conf` に設定されてるせい。 `HandleLidSwitch=ignore` にすることで無効にする。



network
-------


無線を使うわけでなく、ネットワークが突然切れる可能性があるサーバなので、 wicd やめて ifplugd 使うことにした

[Network Configuration - ArchWiki](https://wiki.archlinux.org/index.php/Network_Configuration)

    $ sudo pacman -S ifplugd
    $ sudo systemctl enable ifplugd@eth0.service
    $ sudo systemctl enable dhcpcd@eth0
    $ sudo systemctl disable wicd.service
