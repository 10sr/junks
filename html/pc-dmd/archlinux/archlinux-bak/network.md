# aspireone

* `$ lspci -nn | grep Broadcom`

>`01:00.0 Network controller [0280]: Broadcom Corporation BCM4312 802.11b/g LP-PHY [14e4:4315] (rev 01)`

* b43-fwcutterとb43-firmwareを入れる
* `/etc/modprobe.d/b43.conf` を作成し `blacklist wl` と `blacklist b43legacy` と書く
* `/etc/rc.conf` の MODULES に b43 を追加。
* wicd を使っていて、 wl から b43 に変えた場合、インターフェイスの設定がずれてるのでip linkとか見ながら書き換える

***

* pm-utils
    * /etc/pm/power.d/wireless.sh というファイルを作り、 /usr/sbin/iwconfig wlan0 power off と書いて実行権限を付与
* wicd
    * Acer AspireOneにおいて問題がある模様 → [wicd before connecting reload wlan module — Gist](https://gist.github.com/2133000)
    * → ドライバを b43 にしたら不要になった気がするので無効にしてみる
* laptop-mode tools
    * 無線LANがつながらなくなったので、/etc/laptop-mode/conf.d内にあるwireless系の3つの設定を無効
    * → ドライバを wl から b43 に変えたら動くようになったので、３つをautoに戻す。
    * → やっぱりダメかも。 0 にする。

* ipv6 が原因かもしれないという記述を見たので、 /boot/grub/menu.lst に ipv6.disable=1 を追加してみる

### wlan0: deauthenticating from by local choice (reason=3)

[Random disconnecting | Wicd - ArchWiki](https://wiki.archlinux.org/index.php/Wicd#Random_disconnecting)

***
参考

[b43 - Linux Wireless](http://linuxwireless.org/en/users/Drivers/b43)

### forum

[wicd doesn't scan for network, last resort. (Page 2) / Newbie Corner / Arch Linux Forums](https://bbs.archlinux.org/viewtopic.php?id=139265&p=2)

[[SOLVED] not sure where i'm going wrong with broadcom-wl drivers... (Page 1) / Laptop Issues / Arch Linux Forums](https://bbs.archlinux.org/viewtopic.php?id=117035)

### wiki

[Broadcom wireless - ArchWiki](https://wiki.archlinux.org/index.php/Broadcom_wireless)

[Wicd - ArchWiki](https://wiki.archlinux.org/index.php/Wicd)

[Acer Aspire One - ArchWiki](https://wiki.archlinux.org/index.php/Acer_Aspire_One)

[Acer Aspire One D250 - ArchWiki](https://wiki.archlinux.org/index.php/Acer_Aspire_One_D250)

[14e4:4315]

# lets note

## wired

1. ip link set eth0 up
2. dhcpcd eth0

## wireless

* インテル® Centrino® Advanced-N + WiMAX 6250
* wlp2s0
* wireless_tools, iw
* lspci -v すると、 Kernel driver に iwlwifi が使われてて、なんかできてるように見える？
* ip link set wlp2s0 up しても UP にはならない。そのまま dhcpcd wlp2s0 すれば良い。
* [Wicd - ArchWiki](https://wiki.archlinux.org/index.php/Wicd)

wifi-menu するとなんかできる？
