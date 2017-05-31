[../index.html](../index.html)

## [Arch](https://wiki.archlinux.org/index.php/Main_Page)

<http://togetter.com/li/269698>

古いの：<https://www.jottit.com/z45qk/>

***
## [AUR](https://wiki.archlinux.org/index.php/AUR) からのインストール
ダウンロードしたパッケージを展開し、PKGBUILDとinstallを編集。

    $ makepkg -s
    # pacman -U package.pkg.tar.gz

* <http://d.hatena.ne.jp/sr10/20120317/1331960857>

***
## tips

### ディスプレイを30minアイドルでブランクに
* `xset s 1800`
* `xset dpms 1810 1820 1830`
* この4つの違いが分からない。見た目では変わらないけど違いあるんだろうか？

### コンソールのキーマップ
`/usr/share/kbd/keymaps`あたりのファイルを編集し、`/etc/vconsole.conf`に設定

* capslockをctrlに : change the line `keycode 58 = Caps_Lock` to `keycode 58 = Control`
* backspaceがemacsで動くように修正
* 結果→[capslock as ctrl, fix backspace for emacs — Gist](https://gist.github.com/2007521)
* showkey を使うことで、キーコードみたいなのを調べられる

### `# gpasswd -a yourusername group`

* gid=100(users)
* groups=100(users),7(lp),10(wheel),19(log),50(games),91(video),92(audio),
93(optical),95(storage),96(scanner),98(power),108(vboxusers)

### `/etc/rc.local.shutdown`
`pacman-optimize`を追加？

### [Disable Clearing of Boot Messages - ArchWiki](https://wiki.archlinux.org/index.php/Disable_Clearing_of_Boot_Messages#Disable_clearing_by_getty)
`/etc/inittab`のagettyに`--noclear`オプションを加える。`/etc/issue`の変更は不要だった。

### pacman
* pacman-color
* [Pacmatic: Get emails about pending system updates with cron-pacmatic](http://kmkeen.com/pacmatic/index.html)
* [pacmanのキーサーバを設定する - 冷凍庫](http://d.hatena.ne.jp/sr10/20120311/1331446584)
* pacman.conf
    * uncomment UseSyslog
    * ILiveCandy
* yaourt
    * /tmpをtmpfsでマウントしてたりすると領域が足りなかったりするのでそのときは--tmp <dir>とかつける

### syslog-ng.conf
* log everything to tty12

### [tmpディレクトリの自動掃除 - satospo](http://satospo.sakura.ne.jp/blog_archives/tech/linux/tmp.html)
* 必要なんだろうか？様子見

### マジックsysrq
* まず、 /etc/sysctl.conf で kernel.sysrq = 1 に書き換える
* alt+sysrqを押しながら、reisubで再起動

### swap file [Swap - ArchWiki](https://wiki.archlinux.org/index.php/Swap#Swap_file)
* `# fallocate -l 2G /2g.swap`
* `# chmod 600 /2g.swap`
* `# mkswap /2g.swap`
* `# swapon /2g.swap` で終了するまでスワップが有効になる
* `/etc/fstab` に `/2g.swap none swap defaults 0 0` を追記。

### sudo

1. visudo で `%wheel      ALL=(ALL) ALL` を有効化
2. `gpasswd -a usename wheel`

### [コンソールフォント](https://wiki.archlinux.org/index.php/Fonts#Console_fonts) # なんかできない…

`/etc/vconsole.conf` に以下を記述

    FONT="LatGrkCyr-8x16"

`/etc/mkinitcpio.conf` の HOOKS に consolemap を追

`#mkinitcpio -p linux`

***

## memo
* `/usr/local`は基本的に使われない。だいたい`/usr`以下に配置される
