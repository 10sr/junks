/* example-start frame frame.c */

#include <gtk/gtk.h>

int main( int   argc,
          char *argv[] )
{
  /* GtkWidget は ウィジェットのストレージクラス */ 
  GtkWidget *window;
  GtkWidget *frame;
  GtkWidget *button;
  gint i;

  /* GTK の初期化 */
  gtk_init(&argc, &argv);
    
  /* 新しくウィンドウを作成 */
  window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
  gtk_window_set_title(GTK_WINDOW(window), "Frame Example");

  /* "destroy" イベントにシグナルハンドラを接続 */ 
  gtk_signal_connect (GTK_OBJECT (window), "destroy",
                      GTK_SIGNAL_FUNC (gtk_main_quit), NULL);

  gtk_widget_set_usize(window, 300, 300);
  /* ウィンドウのボーダ幅を設定 */
  gtk_container_set_border_width (GTK_CONTAINER (window), 10);

  /* フレームを作成 */
  frame = gtk_frame_new(NULL);
  gtk_container_add(GTK_CONTAINER(window), frame);

  /* フレームのラベルを設定  */
  gtk_frame_set_label( GTK_FRAME(frame), "GTK Frame Widget" );

  /* ラベルをフレームの右端に設定 */
  gtk_frame_set_label_align( GTK_FRAME(frame), 1.0, 0.0);

  /* フレームのスタイルを設定 */
  gtk_frame_set_shadow_type( GTK_FRAME(frame), GTK_SHADOW_ETCHED_OUT);

  gtk_widget_show(frame);
  
  /* ウィンドウを表示 */
  gtk_widget_show (window);
    
  /* イベントループ */
  gtk_main ();
    
  return(0);
}
/* example-end */
