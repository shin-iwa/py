class Main {
  public static void main(String[] args) {

    for(int i = 1; i <= 10; i++) {
      System.out.println(i + "回目のループです");
    }

    String[]names = {"ichieo", "haruka", "jiro"};
    for(String name: names){
      System.out.println(name);
    }
  }
}