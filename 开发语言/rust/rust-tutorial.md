# Rust 教程

## 安装 Rust

### Linux / MacOS 安装 rustup

```bash
$ curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```

### VSCode 插件推荐

* Even Better TOML: 格式化 TOML
* Error Lens: 显示错误
* One Dark Pro: 主题
* CodeLLDB: 调试

### 认识 Cargo
cargo 是 Rust 的包管理器，类似于 npm 或 yarn。cargo 提供了许多命令，用于创建、构建、测试、运行和发布 Rust 项目。
``` text
Commands:
    build, b    Compile the current package
    check, c    Analyze the current package and report errors, but don't build object files
    clean       Remove the target directory
    doc, d      Build this package's and its dependencies' documentation
    new         Create a new cargo package
    init        Create a new cargo package in an existing directory
    add         Add dependencies to a manifest file
    remove      Remove dependencies from a manifest file
    run, r      Run a binary or example of the local package
    test, t     Run the tests
    bench       Run the benchmarks
    update      Update dependencies listed in Cargo.lock
    search      Search registry for crates
    publish     Package and upload this package to the registry
    install     Install a Rust binary
    uninstall   Uninstall a Rust binary
```

#### Cargo.toml 和 Cargo.lock
`Cargo.toml`和`Cargo.lock`是cargo的两个重要文件。
* cargo.toml 是 carogo 特有的项目数据描述文件。它存储了项目的所有元配置信息。
* cargo.lock 是一个记录了项目依赖的文件。它记录了项目依赖的具体版本。
> 什么情况下该把 cargo.lock 上传到 git 仓库里呢？ 当你的项目是一个可运行的程序时，就上传 cargo.lock，如果是一个依赖库项目，那么就添加到 .gitignore 中。

### 下载依赖慢

* 科学上网
* 修改镜像地址

#### 修改 Rust 的下载镜像为国内的镜像地址
在 $HOME/.cargo/config.toml 添加以下内容：

```
[source.crates-io]
replace-with = 'ustc'

[source.ustc]
registry = "git://mirrors.ustc.edu.cn/crates.io-index"

```
创建一个新的镜像源 [source.ustc]，然后将默认的 crates-io 替换成新的镜像源: replace-with = 'ustc'。

### 下载卡住
下载卡住其实就一个原因：下载太慢了。

根据经验来看，卡住不动往往发生在更新索引时。毕竟 Rust 的包越来越多，索引也越来越大，如果不使用国内镜像，卡住还蛮正常的，好在，我们也无需经常更新索引.

Blocking waiting for file lock on package cache

不过这里有一个坑，需要大家注意，如果你同时打开了 VSCODE 和命令行，然后修改了 Cargo.toml，此时 VSCODE 的 rust-analyzer 插件会自动检测到依赖的变更，去下载新的依赖。

在 VSCODE 下载的过程中（特别是更新索引，可能会耗时很久），假如你又在命令行中运行类似 cargo run 或者 cargo build 的命令，就会提示一行有些看不太懂的内容：

```
$ cargo build
    Blocking waiting for file lock on package cache
    Blocking waiting for file lock on package cache
```

其实这个报错就是因为 VSCODE 的下载太慢了，而且该下载构建还锁住了当前的项目，导致你无法在另一个地方再次进行构建。

解决办法也很简单：

增加下载速度，见前面内容
耐心等待持有锁的用户构建完成
强行停止正在构建的进程，例如杀掉 IDE 使用的 rust-analyzer 插件进程，然后删除 $HOME/.cargo/.package_cache 目录

## Rust 基础
