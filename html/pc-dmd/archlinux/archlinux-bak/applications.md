<https://wiki.archlinux.org/index.php/List_of_Applications>

daemons
=======

systemdに移行したあたりで変わった部分があるかも

## acpid

電源の動作を設定するデーモン。電源ボタンの動作、ノートPCを閉じたときの動作とかも設定できる。

## pm-utils

suspend, hibernateなどの動作を細かく設定できる。pm-suspendとかの動作には管理者権限が必要。

## cpufrequtils

cpuの周波数を操作するデーモン

## dbus

なんかいろんなアプリケーションで使われるメッセージシステム。

## udev

ユーザによるディスクのマウント (HALはobsolete)

## policykit

## upower

一般ユーザが電源落とすのに必要かも

## locate

[mlocate](http://carolina.mff.cuni.cz/~trmac/blog/mlocate/)
をインストールする

## laptop-mode tools

ノートPCでの省電力とかの設定をうまくやるもの？
acpidとかcpufrequtilsとかと連携する

## [Secure Shell](https://wiki.archlinux.org/index.php/Secure_Shell)

* pacman -S openssh
* systemctl enable sshd.service
* PasswordAuthentication yes

* → [wlan](wlan)
* [[SOLVED]laptop-mode: failed - udev not active? (Page 1) / Laptop Issues / Arch Linux Forums](https://bbs.archlinux.org/viewtopic.php?pid=1066184#p1066184)
のとおりに、`/usr/share/laptop-mode-tools/modules/hdparm`のはじめの辺りにある`/sbin/udevadm`を`/usr/bin/udevadm`に書き換え
* /etc/laptop-mode/conf.d/dpms-standby.conf で

        BATT_DPMS_STANDBY=300
        LM_AC_DPMS_STANDBY=1800
        NOLM_AC_DPMS_STANDBY=1800
を設定

## cron

* はじめから入ってる
* ローカルでメール送りつけるようなのは多分[ここらへん](https://wiki.archlinux.org/index.php/Local_Mail_Delivery_with_Postfix)参照。

# テキスト系の

* bash-completion
* links
* htop
* unp
* convmv
* archey / alsi
* vlock
* sl
* e3
* slurm
* glances
* ncdu
* [source-highlight](http://www.geocities.jp/harddiskdive/source-highlight/)
    * [Syntax highlighting in LESS](http://judsonsnotes.com/notes/index.php?option=com_content&view=article&id=564:syntax-highlighting-in-less&catid=37:tech-notes&Itemid=59)

## player

* moc xmms2
* cmus
* mpg123


# desktop applications

基本的にあんまり大きくないもの

* wicd : see [wlan](wlan)
* libnotify notify-sendがある
* [Wireshark](https://wiki.archlinux.org/index.php/Wireshark)
* gksu
* gpicview
* gthumb
* baobab
* leafpad
* evince
* file-roller
* audacious / deadbeef
* gstreamer0.10-plugins
* udisks - udevのラッパーみたいなもの？よく分かってない。
とりあえずこれ入れると、pcmanfmとかでディスクの一般ユーザでのマウントができるようになる
* pcmanfm
    * [PCManFM Trashcan not working? - ArchWiki](https://wiki.archlinux.org/index.php/Pcmanfm#Trashcan_not_working.3F)
        * gvfsをインストール
        * ~/.xinitrc に `exec ck-launch-session dbus-launch openbox-session`
* dropbox
    * 設定でシステム起動時に起動を有効にすると、~/.config/autostart/dropbox.desktopが生成される
* pinta
* mtpaint
* rubyroom

## openbox

* lxappearance
    * simple-icon-theme
* tint2
    * [gsimplecal](https://github.com/dmedvinsky/gsimplecal)
    * volumeicon
* dmenu
* feh
* obmenugen-bin
    * インストールしたら既存のmenu.xmlをバックアップしておく。
    * `$ obmenugen` とすればmenu.xmlがpipeを使ってメニューを自動生成するように書き換えられる。
    * [wiki](https://wiki.archlinux.org/index.php/Openbox_Themes_and_Apps#Logout_dialog)
    からコピーしたexit-menuを付け加える。
    * 最終的な状態：
    [obmenugen generated menu for openbox — Gist](https://gist.github.com/2101119#comments)
    * rc.xmlにはこう：
    [openbox configuration newly added codes — Gist](https://gist.github.com/1998681)
* [Xcompmgr - ArchWiki](https://wiki.archlinux.org/index.php/Xcompmgr)
    * xcompmgrを入れて、xcompmgr -cするだけ。
    * とりあえず起動時に設定したけど常用するかは様子見

## fonts

* 日本語フォント monapo
* その他、
ttf-freebanglafont
ttf-myanmar3
ttf-khmer
ttf-malayalam-fonts
ttf-lklug
ttf-tamil
ttf-tlwg
ttf-tibetan-machine
opendesktop-fonts
ttf-baekmuk
* ~/.fonts.conf　に　[my font config — Gist](https://gist.github.com/2051565)　のように書いた。

## [Xdg-open - ArchWiki](https://wiki.archlinux.org/index.php/Xdg-open)

多分普通はpcmanfmで開いたほうが良い

まず、 xdg-mime query filetype a.txt と xdg-mime query default text/plain を調べる。
それがないと、mimeopenを使う。設定はxdg-mimeよりmimeopenのほうがずっと楽。

1. `perl-file-mimeinfo`をインストール
2. パスが通ってないので、ログアウトするかmimeopenを探す。
2. `$ mimeopen -d file.ext` で開くプログラムが設定できる。
3. これ以降は、xdg-openでも上で設定したプログラムで開かれるようになる。


## python-gtk

### python-gtk2

* python2 じゃないと使えない？

### gtk3 (gobject)

gtk3, python-gobject を入れる。

gobject, gobject2 があり、それぞれ py2, py3k のパッケージがある（計４つ）。普通は gobject を使えば良い？

***

# 入れるか迷ってるもの

* prey
* kupfer
* bmon
* furiusisomount
* acetoneiso
* [xfumble](http://endoh-namazu.tierra.ne.jp/xfumble/about_xfumble.html)
* speedometer
* nmon
* dstat

## [Cool, but obscure unix tools :: Software architect Kristof Kovacs](http://kkovacs.eu/cool-but-obscure-unix-tools)
