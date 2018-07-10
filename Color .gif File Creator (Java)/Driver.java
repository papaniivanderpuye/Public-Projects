

import java.awt.image.BufferedImage;
import java.awt.image.WritableRaster;
import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.Random;
import java.util.InputMismatchException;

class Driver{
	private final static String fName = "palette.gif";

	public static void main(String[] args){


		// Temporary test
		ColorPalette myCP2 = new ColorPalette();

		myCP2.add(new Color(Color.RED));
		boolean result = myCP2.contains(new Color(Color.RED));
		System.out.println(myCP2);
		System.out.println("result: " + result);



		String ansS;
		int ansI;
		Scanner myScanner = new Scanner(System.in);
		ColorPalette myColorPalette = null;

		System.out.println("Would you like to make a custom color palette?");
		System.out.print(": ");
		ansS = myScanner.nextLine();
		if(ansS.equals("n") || ansS.equals("N")){
			System.out.println("Using default color palette.");
			myColorPalette = ColorPalette.makeDefaultColorPalette();

		} else if (ansS.equals("y") || ansS.equals("Y")){
			System.out.println("Great!  Let's add some colors!");
			myColorPalette = new ColorPalette();

			while(true){
				showMenu();
				ansI = getIntInput(myScanner, 1, 7);
				System.out.println("ansI: " + ansI);

				if(ansI == 7){
					break;
				} else {
					doChoice(ansI, myColorPalette, myScanner);
				}
			}

		} else {
			System.out.println("Invalid selection, quitting.");
			System.exit(1);
		}


		if(myColorPalette.size() == 0){
			System.out.println("No colors in palette.  quitting.");
			System.exit(0);
		}
		output(myColorPalette);
		System.out.println("Palette: " + myColorPalette);

	}

	// Writes a .gif file as output.
	private static void output(ColorPalette palette){
		int width = 300;
		int height = 300;
		BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);

		int numItems = palette.size();
		int secSize = height / numItems;

		WritableRaster raster = image.getRaster();
		for(int i=0; i<width; i++){
		    for(int  j=0; j<height; j++){
		    	int colorIdx = j/secSize;
		    	Color c = palette.get(colorIdx);
        		int[] colorArray = c.toArray();
        		raster.setPixel(i, j, colorArray);
    		}
		}
		try{
			ImageIO.write(image, "gif", new File(fName));
			System.out.println("See " + fName);;
		} catch (IOException e){
			e.printStackTrace();
		}
	}

	private static void showMenu(){
		System.out.println("\nWhat would you like to do?");
		System.out.println("\t1) Custom R, G, B values");
		System.out.println("\t2) Random Color");
		System.out.println("\t3) Add red");
		System.out.println("\t4) Add yellow");
		System.out.println("\t5) Add blue");
		System.out.println("\t6) View current palette");
		System.out.println("\t7) Done");
		System.out.print(": ");

	}

	private static int getIntInput(Scanner s, int lBound, int uBound){
		int ans = lBound - 1;
		while (ans < lBound || ans > uBound){
			try{
				ans = s.nextInt();
			} catch (InputMismatchException e){
				System.out.println("Invalid choice!");
				s.next();
			}
		}
		return ans;
	}

	private static int[] getColorChoice(Scanner s){
		System.out.println("Selecting colors!");
		String[] letters = new String[]{"red: ", "green: ", "blue: "};
		int[] colors = new int[3];
		for(int i = 0; i < letters.length; i++){
			System.out.print(letters[i]);
			int ans = getIntInput(s, 0, 255);
			colors[i] = ans;
		}
		return colors;
	}

	private static void doChoice(int choice, ColorPalette palette, Scanner s){
		Color c;
		switch (choice) {
			case 1:
				int[] colorArray = getColorChoice(s);
				c = new Color(colorArray);
				palette.add(c);
				System.out.println("New color added" + c);
				break;

			case 2:
				c = new Color(rand.nextInt(256),rand.nextInt(256),rand.nextInt(256));
				palette.add(c);
				System.out.println("Random color added" + c);
				break;

			case 3:
				c = new Color(Color.RED);
				palette.add(c);
				System.out.println("Red added");
				break;

			case 4:
				c = new Color(Color.YELLOW);
				palette.add(c);
				System.out.println("Red added");
				break;

			case 5:
				c = new Color(Color.BLUE);
				palette.add(c);
				System.out.println("Red added");
				break;

			case 6:
				System.out.println("Here are the colors added:");
				System.out.println(palette);
				break;
		}
	}
}
