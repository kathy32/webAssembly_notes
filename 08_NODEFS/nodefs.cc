// nodefs.cc
#include <stdio.h>
#include <stdlib.h>
// EM_ASM 需要的包
#include <emscripten.h>

void setup_nodefs() {
  // EM_ASM 括号内表示 js 代码
  EM_ASM(
    FS.mkdir("/data");  // 在虚拟文件系统中创建了“/data”目录
    FS.mount(NODEFS, {root: "."}, "/data"); // 将当前的本地目录挂接到了上述目录 “/data”
  );
}

int main() {
  setup_nodefs();

  FILE *fp = fopen("/data/nodefs_data.txt", "r+t");

  if (fp == NULL) {
    fp = fopen("/data/nodefs_data.txt", "w+t");
  }

  int count = 0;
  if (fp) {
    fscanf(fp, "%d", &count); // 从流 fp 读取格式化输入。
    count++;
    fseek(fp, 0, SEEK_SET); // 查找，设置流 fp 的文件位置为给定的偏移 0，SEEK_SET位置查找的字节数
    fclose(fp);
    printf("count:%dn", count);
  }

  else {
    printf("fopen failed.n");
  }

  return 0;
}

