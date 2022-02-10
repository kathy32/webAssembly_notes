// 打包文件系统
//packfile.cc
// emcc packfile.cc -o packfile.js --preload-file hello.txt -s EXIT_RUNTIME=1
#include <stdio.h>
#include <stdlib.h>

int main() {
  FILE *fp = fopen("hello.txt", "rt");  // t表示文本文档
  if(fp) {
    // 测试给定流 stream 的文件结束标识符
    // 当设置了与流关联的文件结束标识符时，该函数返回一个非零值，否则返回零。
    while (!feof(fp)) { // 没有结束
      char c = fgetc(fp); // 获取下一个字符
      if (c != EOF) { // EOF: 移动到文件末尾
        putchar(c); // 把参数 c 指定的字符写入到标准输出 stdout 中
      }
    }
    fclose(fp);
  }
  return 0;
}