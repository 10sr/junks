/* example-start eventbox eventbox.c */

#include <gtk/gtk.h>

int
main (int argc, char *argv[])
{
    GtkWidget *window;
    GtkWidget *event_box;
    GtkWidget *label;

    gtk_init (&argc, &argv);

    window = gtk_window_new (GTK_WINDOW_TOPLEVEL);

    gtk_window_set_title (GTK_WINDOW (window), "Event Box");

    gtk_signal_connect (GTK_OBJECT (window), "destroy",
                        GTK_SIGNAL_FUNC (gtk_exit), NULL);

    gtk_container_set_border_width (GTK_CONTAINER (window), 10);

    /* イベントボックスを作成し、toplevel ウィンドウに追加する */

    event_box = gtk_event_box_new ();
    gtk_container_add (GTK_CONTAINER(window), event_box);
    gtk_widget_show (event_box);

    /* 長いラベルを作成 */

    label = gtk_label_new ("Click here to quit, quit, quit, quit, quit");
    gtk_container_add (GTK_CONTAINER (event_box), label);
    gtk_widget_show (label);

    /* 長いラベルを短くクリップ */
    gtk_widget_set_usize (label, 110, 20);

    /* 更に、アクションをバインドする */
    gtk_widget_set_events (event_box, GDK_BUTTON_PRESS_MASK);
    gtk_signal_connect (GTK_OBJECT(event_box), "button_press_event",
                        GTK_SIGNAL_FUNC (gtk_exit), NULL);

    /* もう一つ、X ウィンドウに必要なのは ... */

    gtk_widget_realize (event_box);
    gdk_window_set_cursor (event_box->window, gdk_cursor_new (GDK_HAND1));

    gtk_widget_show (window);

    gtk_main ();

    return(0);
}
/* example-end */
