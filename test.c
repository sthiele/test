 
#include <clingo.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char const **argv) {

  int ret = 0;
  char const *error_message;

  clingo_location_t location;
  // initialize the location
  location.begin_line   = location.end_line   = 0;
  location.begin_column = location.end_column = 0;
  location.begin_file   = location.end_file   = "";

  clingo_symbol_t sym;
  // symbol
  if (!clingo_symbol_create_id("test", true, &sym)) { goto error; }

  // term
  clingo_ast_t *term = NULL;
  if (!clingo_ast_build(clingo_ast_type_symbolic_term, &term, &location, sym)) {
    goto error;
  }

  // guard
  clingo_ast_t *guard = NULL;
  if (!clingo_ast_build(clingo_ast_type_guard, &guard, clingo_ast_comparison_operator_greater_than
, term)) {
    goto error;
  }

  size_t n;
  char *str;

  // determine size of the string representation of the AST object
  if (!clingo_ast_to_string_size(guard, &n)) { goto error; }


  // allocate required memory to hold the AST's string
  if (!( str = (char*)malloc(sizeof(*str) *   n))) {
    clingo_set_error(clingo_error_bad_alloc, "could not allocate memory for symbol's string");
    goto error;
  }

  // retrieve the symbol's string
  if (!clingo_ast_to_string(guard, str, n)) { goto error; }

  printf(" %s\n", str);

  goto out;

error:
  if (!(error_message = clingo_error_message())) { error_message = "error"; }

  printf("%s\n", error_message);
  ret = clingo_error_code();

out:

  if (term) { clingo_ast_release(term); }

  return ret;
}
