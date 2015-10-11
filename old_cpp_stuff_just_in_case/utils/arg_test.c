/**
 * To install libargtable2 on Ubuntu: sudo apt-get install libargtable2-dev
 * To compile with libargtable2: add '-largtable2' to your compilation statement
 * 
 * For more: http://argtable.sourceforge.net/example/
 */

#include <stdio.h>
#include <argtable2.h>


int
main(int argc, char** argv) {

  // We declare our arguments in the following way:
  //
  // - we can choose a constructor to indicate if there should be 0 or 1,
  //   exactly 1, or an arbitrary number of values $x$ to $y$ for an argument
  //   based on theconstructor used: arg_<type><n values>
  //
  //    <arg type> <variable>     <constructor>  <short name> <long name> <type hint>  <description>
  struct arg_file* infile       = arg_file1(     NULL,        NULL,       "<file>",    "The input file to be processed.");
  struct arg_file* outfile      = arg_file0(     "o",         NULL,       "<file>",    "output file (default is \"-\")");
  struct arg_int*  debug        = arg_int0(      "d",         "debug",    "<level>",   "Debug level to be used.");
  struct arg_rem*  debug_remark = arg_rem                                 NULL,        "Continued text for the debug option.");
            // ^ the remark type does nothing except hold additional lines of description
  struct arg_lit*  help         = arg_lit0(      "h",         "help",                  "print this help and exit");
            // ^ the literal type is just for the presence of a flag: ./a.out -h
  struct arg_end*  end          = arg_end(20); // end is a special type that
                                               // goes at the end of the table
                                               // and holds info on up to $n$
                                               // arg errors (in this case n=20)

  // put our arguments in a table for processing
  void* arg_table[] = {  // order matters for arguments that weren't
    infile,              // specified without a flag/name, like 'infile', 
    outfile,             // and the order the help message prints...
    debug,
    debug_remark,
    help,
    end                  // ... and for end
  };

  // ensure memory could be allocated properly
  if (arg_nullcheck(arg_table) != 0) {
    puts("The argument table could not be allocated. Something is very wrong.");
    exit(0);
  }

  // set defaults
  // it's recommended practice to set the defaults before doing the actual
  // argument parsing.
  debug->hdr.flag |= ARG_HASOPTVALUE; // this is good for options that will be
                                      // used wether or not the user specifies
                                      // the argument. We need this if we
                                      // don't want an error for the argument
                                      // not being specified.

  debug->ival[0] = 0;                 // each value for a given argument gets
                                      // its own spot in an array, most of the
                                      // time though, we only want one value,
                                      // i.e. the 0th

  // perform the parsing of the arguments
  int error_count = arg_parse(argc, argv, arg_table);
  if (error_count > 0) {
    arg_print_errors(stdout, end, argv[0]);
    exit(0);
  }

  // start extracting the values and taking appropriate action
  if (argc == 1 || help->count > 0) { // the count struct member lets us know
                                      // how many values were provided for an
                                      // argument. In most cases, we just need
                                      // to know 1 or 0.

    // arg_print_syntaxv(stdout, arg_table, "\n");        // prints just the flags for the options
    arg_print_glossary(stdout, arg_table, " %-25s %s\n"); // prints options and glossary (descriptions)
  }

  // Finally, we can use our arguments for something useful, like printing them!
  printf(
    "Input file:  %s (full), %s (base), %s (extension)\n"
    "Output file: %s (full), %s (base), %s (extension)\n"
    "Debug level: %d, (defaulted: %d)\n"
    "Help:        %d\n",
    infile->filename[0], infile->basename[0], infile->extension[0],
    outfile->count == 1 ? outfile->filename[0] : "None specified",
      outfile->count == 1 ? outfile->basename[0] : "None specified",
      outfile->count == 1 ? outfile->extension[0] : "None specified",
    debug->ival[0], debug->count == 0 ? 1 : 0,
    help->count);


  // be sure to free the table when you are completely done with it.
  // this frees up all of the table entries.
  arg_freetable(arg_table, sizeof(arg_table) / sizeof(arg_table[0]));

  // it is possible (and recommended) to provide a callback function to
  // the argument struct if you want to do custom error checking of the args
  // and their values. But that's advanced functionality I won't discuss here.

  return 0;
}
