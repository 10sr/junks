/* example-start helloworld2 helloworld2.c */

#include <gtk/gtk.h>

/* 新たに改良されたコールバック。この関数に渡される data は stdout
 * に表示される。 */
void callback( GtkWidget *widget,
               gpointer   data )
{
    g_print ("Hello again - %s was pressed\n", (char *) data);
}

/* もう一つのコールバック */
void delete_event( GtkWidget *widget,
                   GdkEvent  *event,
                   gpointer   data )
{
    gtk_main_quit ();
}

int main( int   argc,
          char *argv[] )
{
    /* GtkWidget はウィジェットを保持するための型 */
    GtkWidget *window;
    GtkWidget *button;
    GtkWidget *box1;

    /* これは全ての GTK アプリケーションで呼ばれる。コマンドライン
     * からの引数は構文解析され、アプリケーションに返される。 */
    gtk_init (&argc, &argv);

    /* 新しいウィンドウを作成 */
    window = gtk_window_new (GTK_WINDOW_TOPLEVEL);

    /* これは初めて登場する呼び出しである。新しいウィンドウのタイトルを
     * "Hello Buttons!" に設定する */
    gtk_window_set_title (GTK_WINDOW (window), "Hello Buttons!");

    /* ここでは単に delete_event に直ちに GTK を終了させるハンドラを
     * 設定する。 */
    gtk_signal_connect (GTK_OBJECT (window), "delete_event",
                        GTK_SIGNAL_FUNC (delete_event), NULL);

    /* ウィンドウのボーダ幅を設定する。 */
    gtk_container_set_border_width (GTK_CONTAINER (window), 10);

    /* ウィジェットをパックするボックスを作成する。詳細は "パッキング"
     * セクションで説明される。ボックスは全く表示されず、単にウィジェット
     * を配置するためのツールとして使われる。 */
    box1 = gtk_hbox_new(FALSE, 0);

    /* メインウィンドウにボックスを配置する。 */
    gtk_container_add (GTK_CONTAINER (window), box1);

    /* ラベル "Button 1" を持った新しいボタンを作成する。 */
    button = gtk_button_new_with_label ("Button 1");

    /* ボタンがクリックされたら、引数に "button 1" へのポインタを伴う
     * "callback" 関数が呼ばれるよう設定する。 */
    gtk_signal_connect (GTK_OBJECT (button), "clicked",
                        GTK_SIGNAL_FUNC (callback), (gpointer) "button 1");

    /* gtk_container_add の代わりにこのボタンを不可視のボックスにパックする。
     * このボックスはウィンドウの中にパックされたものである。 */
    gtk_box_pack_start(GTK_BOX(box1), button, TRUE, TRUE, 0);

    /* このステップは絶対に忘れないように。これは GTK に対し、このボタンの
     * 準備が完了し表示できるようになったことを伝えるものである。 */
    gtk_widget_show(button);

    /* 同様のステップを繰り返し、第二のボタンを作成する。 */
    button = gtk_button_new_with_label ("Button 2");

    /* 異なった引数として "button 2" へのポインタを渡し、同じコールバック
     * 関数を呼ぶようにする。 */ 
    gtk_signal_connect (GTK_OBJECT (button), "clicked",
                        GTK_SIGNAL_FUNC (callback), (gpointer) "button 2");

    gtk_box_pack_start(GTK_BOX(box1), button, TRUE, TRUE, 0);

    /* ボタンを表示する順番はあまり重要ではない。しかしウィンドウは最後に
     * 表示することをお勧めする。そうすることで全てが一度に画面に現れる。 */
    gtk_widget_show(button);

    gtk_widget_show(box1);

    gtk_widget_show (window);

    /* gtk_main で休止し、始まるのを楽しみに待とう! */
    gtk_main ();

    return(0);
}
/* example-end */
