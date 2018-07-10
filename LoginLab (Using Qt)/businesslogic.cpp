#include "businesslogic.h"
#include <QDebug>

BusinessLogic::BusinessLogic(QObject *parent) : QObject(parent),
    m_loaded(false)
{
    qDebug() << m_loaded;
}

void BusinessLogic::login()
{
    qDebug() << "Logging in";

    QStringList myList;
    myList << "Hello" << "Goodbye" << "Later";

    setLoaded(!m_loaded);

    emit mySignal(myList);
}

void BusinessLogic::signOut()
{
    qDebug() << "Signing Out!";
}

bool BusinessLogic::loaded() const
{
    qDebug() << m_loaded;
    return m_loaded;
}

void BusinessLogic::setLoaded(bool loaded)
{
    if (m_loaded == loaded)
        return;

    m_loaded = loaded;
    emit loadedChanged(m_loaded);
}
