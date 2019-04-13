Pushbullet API
===============

https://github.com/rbrcsk/pushbullet.py


iPhone の通知を正しくやってくれるために
-----------------------------

参考

- https://bohbi-log.com/app/pushbullet/ （リンク切れ）
- https://webcache.googleusercontent.com/search?q=cache:iqtGDz8_i34J:https://bohbi-log.com/app/pushbullet/+&cd=1&hl=ja&ct=clnk&gl=jp&lr=lang_en%7Clang_ja&client=firefox-b-d （グーグルのキャッシュ）


iPhone のアプリを入れても、プッシュ通知を正しくやってくれない場合がある
上記の記事を参考に、以下の手順を踏むことで自分はできるようになった

1. iPhone 自体の設定で、 Pushbullet からの通知が有効になっていることを確認する
2. Pushbullet アプリでサインアウトする
3. Pushbullet アプリでサインインする

上記でうまく行かなかった場合手順３の前に iPhone の設定から Pushbullet の通知設定をオフ→オンとやり直す、といいかもしれない？
