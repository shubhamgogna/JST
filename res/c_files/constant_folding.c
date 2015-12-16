

            const int C = 4+4;

            int main() {

                int n = C-2+4*2; // expect to find a li with 14 in the assembly instructions
                                 // since we have constant folding working correctly
                print_int(n);  // expect to see the 14 printed to show its loaded into n correctly

                return 0;
            }
            