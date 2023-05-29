class LeetCode_1603 {
    public static final int BIG_SIZE = 1;
    public static final int MEDUIM_SIZE = 2;
    public static final int SMALL_SIZE = 3;
    int big;
    int medium;
    int small;

    public LeetCode_1603(int big, int medium, int small) {
        this.big = big;
        this.medium = medium;
        this.small = small;
    }

    public boolean addCar(int carType) {
        if (carType == BIG_SIZE) {
            if (big == 0)
                return false;
            big--;
        }

        if (carType == MEDUIM_SIZE) {
            if (medium == 0)
                return false;
            medium--;
        }

        if (carType == SMALL_SIZE) {
            if (small == 0)
                return false;
            small--;
        }

        return true;
    }
}