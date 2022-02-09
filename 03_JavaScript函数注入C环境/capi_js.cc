// emcc capi_js.cc --js-library pkg.js -o capi_js.js
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

EM_PORT_API(int) js_add(int a, int b);
EM_PORT_API(void) js_console_log_int(int param);

// 在C环境中调用JavaScript方法
EM_PORT_API(void) print_the_answer() {
  int i = js_add(21, 21);
  js_console_log_int(i);
}