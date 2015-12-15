            int main() {

                int i = 0;

                // FizzBuzz
                for( i = 1; i <= 30; i++) {
                   //FizzBuzz
                   if( i % 3 == 0){

                        //FizzBuzz
                        if( i % 5 == 0 ){

                            //print_char('f');
                            //print_char('b');
                            print_int(35);      // expect to see this replacing 15 and 30
                        }

                        //Fizz
                        else {
                           //print_char('f');
                            print_int(3);   // expect to see this replacing 3,6,9,12,18,21,24,27
                        }

                   }
                   // Buzz
                   else if( i % 5 == 0) {
                       //print_char('b');
                       print_int(5);    // expect to see this replacing 5,10,15,20,25

                   }
                   // Number
                   else{
                       print_int(i);    // expect to see all other numbers except those mentioned above
                   }
                }

                return 0;
            }