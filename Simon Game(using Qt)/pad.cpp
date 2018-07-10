#include "pad.h"
#include <stdlib.h>
#include <QTimer>
#include <QDebug>
#include <QList>

Pad::Pad(QObject *parent) : QObject(parent)
{


    mySequence = QString("") ;
    randomSequence =QString("1");
    randomLength = 0;
    currentNum = 0;
    sequenceList={};
    myIndex=0;
    won=false;



    //playlist->addMedia(QUrl("http://example.com/myfile1.mp3"));
    //playlist->addMedia(QUrl("http://example.com/myfile2.mp3"));


    //playlist->setCurrentIndex(1);
    //player->play();



}

QList<int> Pad:: createRandomNumberList() {
    randomSequence.clear();
    sequenceList.clear();
    randomLength++;
    srand(time(NULL));
    for (int i=0 ;i<randomLength;i++){
        int num = rand() % 4 ;
        randomSequence+= QString::number(num);
        sequenceList.append(num);
    }

    return sequenceList;

}

int Pad:: getNum() {
    return currentNum;

}


void Pad:: turnOff() {

    emit lightDown();
    QTimer::singleShot(500, this, SLOT( startAgain()   )    );
}

void Pad:: playButton(){
    won = false;
    startAgain();
}

void Pad:: startAgain() {
    qDebug() <<"wrong";
    emit gameStart();
    if(won){
        randomLength++;
    }
    else{
        randomLength=0;
    }
    myIndex=0;
    mySequence= QString("");

    createRandomNumberList();
    simonSays();


}

void Pad:: turnPadOff() {
    emit playPadOff();
    myIndex++;
    if(myIndex<sequenceList.length() ){
        simonSays();
    }

}


void Pad:: simonSays() {

        currentNum = sequenceList[myIndex];
        emit playPadOn();
        QTimer::singleShot(500, this, SLOT( turnPadOff()   )    );

}


//lightup

//sendindex
void Pad:: win(){
    emit lightUp();
    QTimer::singleShot(400, this, SLOT( turnOff()   )    );
}


void Pad::pressed(int index){

   mySequence += QString::number(index);
   qDebug() << "working";
   qDebug() << mySequence;
   qDebug() << randomSequence;
   if (mySequence.length() == randomSequence.length() ){

       if (mySequence==randomSequence){
           won=true;

           QTimer::singleShot(250, this, SLOT( win()  )    );


       }

       else{

           won=false;
           emit gameOver();

       }


   }




    }
