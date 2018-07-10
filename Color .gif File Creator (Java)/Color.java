

public class Color {

	// public "constants" useful for other classes, never change
	public final static int[] RED = new int[]{255, 0, 0};
	public final static int[] YELLOW = new int[] {255, 255, 0};
	public final static int[] BLUE = new int[] {0, 0, 255};

	// Private instance variables
	private int r;
	private int g;
	private int b;

	// Primary constructor
	public Color(int newR, int newG, int newB){
		r = verify(newR);
		g = verify(newG);
		b = verify(newB);
	}

	// Overloaded constructor (there are two valid constructors)
	public Color()
	{
		this();
	}

	// Validates a color value (between 0 and 255)
	public int verify(int newVal){
		if(newVal < 0 || newVal > 255){
			throw new IllegalStateException("Invalid color value: " + newVal);
		} else {
			return newVal;
		}
	}

	// Getters
	public int r(){
		return r;
	}

	public int g() {
		return g;
	}

	public int b() {
		return b;
	}

	public int[] toArray(){
		return new int[]{r, g, b};
	}


}
