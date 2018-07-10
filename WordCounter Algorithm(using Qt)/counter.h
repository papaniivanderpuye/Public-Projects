#ifndef COUNTER_H
#define COUNTER_H
#include <QObject>

class Counter : public QObject
{
    Q_OBJECT
private:
    bool c,w,l;
    QStringList args;
public:
    explicit Counter( QStringList args1,bool c1 =false , bool w1 = false , bool l1= false,QObject *parent = nullptr);




    int wordCount(QString text);

    int lineCount(QString& text);

    int characterCount(QString& text);

signals:
    //fileChanged(const QFileChanged &);


public slots:

    void update(const QString& str);
    //void update(const QStringList args,bool c, bool w, bool l);



};



#endif // COUNTER_H
