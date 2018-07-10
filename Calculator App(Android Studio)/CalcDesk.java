package edu.fandm.pvanderp.calcdesk;

import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.google.android.gms.appindexing.Action;
import com.google.android.gms.appindexing.AppIndex;
import com.google.android.gms.appindexing.Thing;
import com.google.android.gms.common.api.GoogleApiClient;

import java.util.Stack;

public class CalcDesk extends AppCompatActivity implements View.OnClickListener {

    private final static String TAG = CalcDesk.class.getName();

    private String sentence = "";
    private String numbers = "1234567890.";
    private String firstOrder = "*/";
    private String secondOrder = "+-";


    private TextView tv = (TextView) findViewById(R.id.display);
    private Stack<String> opStack = new Stack();
    private String[] postFix;
    /**
     * ATTENTION: This was auto-generated to implement the App Indexing API.
     * See https://g.co/AppIndexing/AndroidStudio for more information.
     */
    private GoogleApiClient client;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_calc_desk);


        Button one = (Button) findViewById(R.id.one);
        one.setOnClickListener(this);


        Button two = (Button) findViewById(R.id.two);
        two.setOnClickListener(this);

        Button three = (Button) findViewById(R.id.three);
        three.setOnClickListener(this);

        Button plus = (Button) findViewById(R.id.plus);
        one.setOnClickListener(this);

        Button four = (Button) findViewById(R.id.four);
        two.setOnClickListener(this);

        Button five = (Button) findViewById(R.id.five);
        three.setOnClickListener(this);

        Button six = (Button) findViewById(R.id.six);
        one.setOnClickListener(this);

        Button minus = (Button) findViewById(R.id.minus);
        two.setOnClickListener(this);

        Button seven = (Button) findViewById(R.id.seven);
        three.setOnClickListener(this);

        Button eight = (Button) findViewById(R.id.eight);
        one.setOnClickListener(this);

        Button nine = (Button) findViewById(R.id.nine);
        two.setOnClickListener(this);

        Button multipliedBy = (Button) findViewById(R.id.multipliedBy);
        three.setOnClickListener(this);

        Button zero = (Button) findViewById(R.id.zero);
        one.setOnClickListener(this);

        Button point = (Button) findViewById(R.id.point);
        two.setOnClickListener(this);

        Button toThePower = (Button) findViewById(R.id.toThePower);
        three.setOnClickListener(this);

        Button divededBy = (Button) findViewById(R.id.divededBy);
        one.setOnClickListener(this);

        Button enter = (Button) findViewById(R.id.enter);
        two.setOnClickListener(this);

        Button clear = (Button) findViewById(R.id.clear);
        three.setOnClickListener(this);


        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client = new GoogleApiClient.Builder(this).addApi(AppIndex.API).build();
    }

    @Override
    public void onClick(View v) {


        // default method for handling onClick Events..

        switch (v.getId()) {

            case R.id.one:
                sentence += "1";

                tv.setText(sentence);
                // do your code
                break;

            case R.id.two:
                sentence += "2";

                tv.setText(sentence);
                // do your code
                break;

            case R.id.three:
                sentence += "3";

                tv.setText(sentence);
                // do your code
                break;

            case R.id.plus:
                sentence += "+";

                tv.setText(sentence);
                // do your code
                break;

            case R.id.four:
                sentence += "4";

                tv.setText(sentence);
                // do your code
                break;

            case R.id.five:
                sentence += "5";

                tv.setText(sentence);
                // do your code
                break;
            case R.id.six:
                sentence += "6";

                tv.setText(sentence);
                // do your code
                break;

            case R.id.minus:
                sentence += "-";

                tv.setText(sentence);
                // do your code
                break;

            case R.id.seven:
                sentence += "7";

                tv.setText(sentence);
                // do your code
                break;

            case R.id.eight:
                sentence += "8";

                tv.setText(sentence);
                // do your code
                break;

            case R.id.nine:
                sentence += "9";

                tv.setText(sentence);
                // do your code
                break;

            case R.id.multipliedBy:
                sentence += "*";

                tv.setText(sentence);
                // do your code
                break;
            case R.id.zero:
                sentence += "0";

                tv.setText(sentence);
                // do your code
                break;

            case R.id.point:
                sentence += ".";

                tv.setText(sentence);
                // do your code
                break;

            case R.id.toThePower:
                sentence += "^";

                tv.setText(sentence);
                // do your code
                break;
            case R.id.divededBy:
                sentence += "/";

                tv.setText(sentence);
                // do your code
                break;

            case R.id.enter:
                shuntingYard(sentence);
                break;

            case R.id.clear:
                sentence = "0";

                tv.setText(sentence);
                // do your code
                break;

            default:
                break;
        }


    }

/*
    public void addToPostfix(String elem)
    {



        if (numbers.contains(elem))
        {
          postFix += elem;
        }

        else{
                if(opStack.isEmpty())
                {
                opStack.push(elem);
                }

                else
                {
                    String topOperand = opStack.pop();
                    if((firstOrder.contains(topOperand) ) &&  secondOrder.contains(elem) )
                    {
                        postFix += topOperand;
                        opStack.push(elem);

                    }

                    else
                    {
                        opStack.push(topOperand);
                        opStack.push(elem);
                    }


                }
            }
    }
*/


    public void shuntingYard(String sentence)
    {
        int pos = 0;
        postFix = new String[sentence.length()];
        for (int i = 0 ; i < sentence.length() ; i++)
        {
            char c = sentence.charAt(i);
            String elem = String.valueOf(c);

            if (numbers.contains(elem))
            {
                postFix[i] += elem;
            }

            else
            {
                if(opStack.isEmpty())
                {
                    opStack.push(elem);
                }

                else
                {
                    String topOperand = opStack.pop();
                    if((firstOrder.contains(topOperand) ) &&  secondOrder.contains(elem) )
                    {
                        postFix[i] = topOperand;
                        opStack.push(elem);

                    }

                    else
                    {
                        opStack.push(topOperand);
                        opStack.push(elem);
                    }


                }
            }

            pos += 1;
        }

        while(!(opStack.isEmpty()) )
        {
            String topOperand = opStack.pop();
            postFix[pos] += topOperand;
            pos += 1;

        }

    }


    public double compute(String[] postFix) throws IllegalArgumentException
    {

    }

    /**
     * ATTENTION: This was auto-generated to implement the App Indexing API.
     * See https://g.co/AppIndexing/AndroidStudio for more information.
     */
    public Action getIndexApiAction() {
        Thing object = new Thing.Builder()
                .setName("CalcDesk Page") // TODO: Define a title for the content shown.
                // TODO: Make sure this auto-generated URL is correct.
                .setUrl(Uri.parse("http://[ENTER-YOUR-URL-HERE]"))
                .build();
        return new Action.Builder(Action.TYPE_VIEW)
                .setObject(object)
                .setActionStatus(Action.STATUS_TYPE_COMPLETED)
                .build();
    }

    @Override
    public void onStart() {
        super.onStart();

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client.connect();
        AppIndex.AppIndexApi.start(client, getIndexApiAction());
    }

    @Override
    public void onStop() {
        super.onStop();

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        AppIndex.AppIndexApi.end(client, getIndexApiAction());
        client.disconnect();
    }
}
