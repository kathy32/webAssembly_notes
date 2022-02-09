// mem.cc
// 如何在JavaScript中访问C/C++环境内存
// emcc mem.cc -o mem.js

// 定义EM_PORT_API宏
#ifndef EM_PORT_API
// __EMSCRIPTEN__: 探测是否是Emscripten环境
#	if defined(__EMSCRIPTEN__)
#		include <emscripten.h>
// __cplusplus: 探测是否C++环境
#		if defined(__cplusplus)
#			define EM_PORT_API(rettype) extern "C" rettype EMSCRIPTEN_KEEPALIVE
#		else
// EMSCRIPTEN_KEEPALIVE: Emscripten特有的宏，用于告知编译器后续函数在优化时必须保留，并且该函数将被导出至JavaScript
#			define EM_PORT_API(rettype) rettype EMSCRIPTEN_KEEPALIVE
#		endif
#	else
#		if defined(__cplusplus)
#			define EM_PORT_API(rettype) extern "C" rettype
#		else
#			define EM_PORT_API(rettype) rettype
#		endif
#	endif
#endif

#include <stdio.h>

int g_int = 42;
double g_double = 3.1415926;

EM_PORT_API(int*) get_int_ptr() {
  return &g_int;
}

EM_PORT_API(double*) get_double_ptr() {
  return &g_double;
}

EM_PORT_API(void) print_data() {
  printf("C{g_int: %d}\n", g_int);
  printf("C{g_double: %f}\n", g_double);
}