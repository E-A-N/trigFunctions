using System;
namespace ConsoleApplication{

    public class Triangle{

        private const int angle1;
        private const int angle2;
        private const int angle3;
        private const int oppositeLength;
        private const int adjacentLength;
        private const int valid;

        public void setAngles(int a1, int a2, int a3){
            this.angle1 = a1;
            this.angle2 = a2;
            this.angle3 = a3;
        }

        private bool validateAngles(){
            bool validate;
            int area = this.angle1 + this.angle2 + this.angle1;

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
        public static int sine(int x, int y){
            //hypotenuse
            int r = (x * x) + (y * y);

            return r;

        }


        public static void Main(){
            Console.WriteLine("Hello World!");
        }
    }
}
