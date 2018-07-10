#ifndef PAD_H
#define PAD_H
#include <QObject>
#include <QList>
//#include QAid



class Pad : public QObject
{
    Q_OBJECT

private:
    QString mySequence;
    QString randomSequence;
    int currentNum;
    QList<int> sequenceList;
    int myIndex;
    int randomLength;
    bool won;
    //QMediaPlayer player;
    //QMediaPlaylist playlist = new QMediaPlaylist(player);

public:
    explicit Pad(QObject *parent = nullptr);
    Q_INVOKABLE void pressed(int);
    Q_INVOKABLE QList<int> createRandomNumberList( );
    Q_INVOKABLE void simonSays();
    Q_INVOKABLE int getNum();
    Q_INVOKABLE void win();
    Q_INVOKABLE void playButton();





signals:
   Q_INVOKABLE void  lightUp() ;
   Q_INVOKABLE void  lightDown() ;
   Q_INVOKABLE void  gameOver() ;
   Q_INVOKABLE void gameStart();
   Q_INVOKABLE void playPadOn();
   Q_INVOKABLE void playPadOff();


public slots:
    Q_INVOKABLE void  turnOff() ;
    Q_INVOKABLE void turnPadOff();
    Q_INVOKABLE void startAgain();





};

#endif // PAD_H
