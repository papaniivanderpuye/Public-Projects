function translate(x, y)
{
    x = x - main.width/2
    y = main.height/2 - y
    return Qt.point(x,y)
}

function angletoCoordinate( angle, radius )
{

    var aspectDistance = Math.min( main.width , main.height )
    var x = Math.cos(angle) * (radius * (aspectDistance/2))
    var y = Math.sin(angle) * (radius * (aspectDistance/2))

    //translate
    x = x + main.width/2
    y = main.height/2 - y

    return Qt.point(x,y)
}

function coordinatetoAngle(x,y)
{
    var coordinate = translate(x,y)
    var angle = Math.atan(coordinate.y/ coordinate.x)
    var result

    //extracting angle in Radiant
    if( coordinate.x > 0 )
        if ( coordinate.y > 0)
            result = angle
        else
            result = 2 * Math.PI + angle
    else
        result = Math.PI + angle

    return result
}

function indextoAngle(index, count)
{
    var angle = index/count  * (2*Math.PI)

    var y = Math.cos(angle)
    var x = Math.sin(angle)
}

function coordinatetoIndex(x,y)
{
    var angle = coordinatetoAngle(x,y)
    return( Math.floor((angle/ (2 * Math.PI)) * 4))
}

