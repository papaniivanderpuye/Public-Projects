#include "simon.h"
#include <QTimer>
#include <QDebug>

// Brain of Simon

Simon::Simon(QObject *parent) : QObject(parent)
{
    srand(time(NULL));
}


bool Simon::verify(void)
{
    return true;
}

