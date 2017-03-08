using System;
namespace ConsoleApplication{

    public class Triangle{

        private  int angle1;
        private  int angle2;
        private  int angle3;
        private  int oppositeLength;
        private  int adjacentLength;
        private  int valid;

        public void setAngles(int a1, int a2, int a3){
            this.angle1 = a1;
            this.angle2 = a2;
            this.angle3 = a3;
            this.validateAngles();
        }

        private bool validateAngles(){
            bool validate;
            int area = this.angle1 + this.angle2 + this.angle3;

            if (area == 180){
                validate = true;
            }
            else{
                validate = false;
            }
            return validate;
        }

    }

    public class TrigFuncs {
        public static int sine(int x, int y, Triangle tri){
            //hypotenuse
            int r = (x * x) + (y * y);
            return r;
        }


        public static void Main(){
            Console.WriteLine("Hello World!");
        }
    }
}
