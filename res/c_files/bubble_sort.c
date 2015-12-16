
            const int N_ITEMS = 5;

            int bubble_sort(int things[])
            {
              int i, j, temp;

              print_int(things[0]);  // expect to see 5
              print_char('\n');
              print_int(things[1]);  // expect to see 1
              print_char('\n');
              print_int(things[2]);  // expect to see 4
              print_char('\n');
              print_int(things[3]);  // expect to see 3
              print_char('\n');
              print_int(things[4]);  // expect to see 2
              print_char('\n');

              for (i = 0; i < N_ITEMS; i++) {
                for (j = i; j < N_ITEMS; j++) {
                  if (things[i] < things[j]) {
                    temp = things[i];
                    things[i] = things[j];
                    things[j] = temp;
                  }
                }
              }

              print_char('\n');
              print_int(things[0]);  // expect to see 5
              print_char('\n');
              print_int(things[1]);  // expect to see 4
              print_char('\n');
              print_int(things[2]);  // expect to see 3
              print_char('\n');
              print_int(things[3]);  // expect to see 2
              print_char('\n');
              print_int(things[4]);  // expect to see 1
            }

            int main() {
              int things[N_ITEMS] = {5, 1, 4, 3, 2};

              bubble_sort(things);

              return 0;
            }
            