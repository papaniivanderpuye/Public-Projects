package com.example.loaner.mario;

import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Rect;

import java.util.Random;

/**
 * Created by loaner on 4/18/17.
 */

public class Sprite {
    private static final int BMP_ROWS = 4;
    private static final int BMP_COLUMNS = 3;
    private int x = 0;
    private int y = 0;
    private int xSpeed = 5;
    private GameView gameView;
    private Bitmap bmp;
    private int currentFrame = 0;
    private int width;
    private int height;
    private int ySpeed;
    private boolean isMoving;

    public Sprite(GameView gameView, Bitmap bmp) {
        this.gameView = gameView;
        this.bmp = bmp;
        this.width = bmp.getWidth() / BMP_COLUMNS;
        this.height = bmp.getHeight() / BMP_ROWS;
        Random rnd = new Random();
        xSpeed = rnd.nextInt(10)-5;
        ySpeed = rnd.nextInt(10)-5;
    }

    private void update() {
        if(isMoving)
        {
            /*
            x = x + xSpeed;
            if (y > gameView.getHeight() - height - ySpeed || y + ySpeed < 0) {
                ySpeed = -ySpeed;
            }
            y = y + ySpeed;
            currentFrame = ++currentFrame % BMP_COLUMNS;
            */
        }
    }

    public void onDraw(Canvas canvas) {
        update();
        int srcX = currentFrame * width;
        int srcY = 2 * height;
        Rect src = new Rect(srcX, srcY, srcX + width, srcY + height);
        Rect dst = new Rect(x, y, x + width, y + height);
        canvas.drawBitmap(bmp, src, dst, null);
    }

    public Rect getBounds(){
        return new Rect(x, y, x+width, y+height);
    }

    /*
    public void checkCollisionBrick(Sprite b){
        Rect mySprite = this.getBounds();
        Rect myCollisionObject = b.getBounds();
        if(mySprite.intersect(myCollisionObject)){
            //Todo code here
            if (y > 0)
            self.numJumps = 0
            self.getImageStand()
            self.rect.bottom = block.rect.top
            if self.changeX == 0:
            self.calcGrav()

            elif self.changeY < 0:
            self.rect.top = block.rect.bottom
            if isinstance(block,bricks.Bricks):
            self.playSoundBR()
            block.goUp()
            self.rect.y += 22

            elif isinstance(block,bricks.QuestionBricks):
            if block.producedCoins == False:
            self.playSoundC()

                        else:
            self.playSoundB()
            block.hitAlready()
            block.goUp()

            self.rect.y += 22


            self.changeY = 0
        }
    }
    */


}