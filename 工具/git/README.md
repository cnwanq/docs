# 玩转 Git

## Git 基础

### Git 的特点
* 最优的存储能力
* 非凡的性能
* 开源的
* 很容易做备份
* 支持离线操作
* 很容易定制工作流程

### 安装 Git
[Git 安装教程](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD)

### Git 最小配置
```bash
git config --global user.name "your name"
git config --global user.email "<EMAIL>"
```
#### config 的三个作用域
缺省为 local，作用域越大权限越大。
```bash
git config --local  # 当前仓库
git config --global # 当前用户
git config --system # 系统所有用户
```

显示 config 的配置，加 --list 参数
```bash
git config --list --local
git config --list --global
git config --list --system
```

### 创建 Git 仓库
两种场景：
1. 把已有的项目代码纳入 Git 管理
```bash
cd existing_project
git init
```
2. 新建的项目直接用 Git 管理
```bash
cd project_directory
git init your_project
cd your_project
```

### 往仓库里添加文件
工作目录 -> 暂存区 -> 仓库(版本管理)


### 给文件重命名的简便方法
1. 修改文件名 old_file -> new_file
2. 执行 git add new_file 命令
3. 执行 git rm old_file 命令
```bash
mv old_file new_file
git add new_file
git rm old_file
```

* 也可以直接执行 git mv old_file new_file 命令

### 通过 git log 查看版本历史
```bash
git log --oneline # 简洁显示
git log --graph   # 图形化显示
git log -n4       # 显示最近的4次提交
```

### 图形界面查看版本历史 - gitk
```bash
gitk
```
其他可视化工具：gitg、SourceTree

### 揭秘 .git 目录
```bash
COMMIT_EDITMSG  # 提交信息
FETCH_HEAD      # 远程分支
HEAD            # 当前分支
ORIG_HEAD       # 合并前的分支
config          # Git 配置
description     # Git 仓库描述
hooks           # Git 钩子
index           # 暂存区
info            # Git 信息
logs            # 提交日志
objects         # 对象库
packed-refs     # 打包的引用
refs            # 引用
```

### commit、tree 和 blob 对象
* commit 对象
  * 记录一次提交操作
  * 包含作者、提交者、日期和提交信息
  * 指向一个 tree 对象
  * 可以有多个父提交
* tree 对象
  * 记录路径和 blob 对象的索引
  * 记录文件修改状态
  * 记录文件名
* blob 对象
  * 记录文件内容


## 使用 Git 常见场景

### 删除分支
```bash
git branch -d your_branch # 删除本地分支
git branch -D your_branch # 强制删除本地分支
```

### 修改最新 commit message
```bash
git commit --amend -m "new message"
```

### 修改历史 commit message
```bash
git rebase -i HEAD~3 # 修改最近3次提交
pick 24587  # 修改指定提交

git rebase -i 24587  # 修改指定提交
```

### 把连续多提交合并成一个
```bash
git rebase -i HEAD~3 # 修改最近3次提交
pick 24587  # 修改指定提交
squash 12369  # 合并到上一个提交
```

### 把间隔多提交合并成一个
```bash
git rebase -i HEAD~3 # 修改最近3次提交
pick 24587  # 修改指定提交
squash 12369  # 合并到上一个提交
pick 45678  # 修改指定提交
squash 34567  # 合并到上一个提交
```

### 比较暂存区和 HEAD 文件差异
```bash
git diff --cached 
# 或者
git diff --staged
```

### 比较工作区和暂存区文件差异
```bash
git diff
```

### 暂存区恢复成和 HEAD 一样
```bash
git reset HEAD --hard
```

### 工作区恢复成和暂存区一样
```bash
git checkout -- .
```

### 取消暂存区部分文件的修改
```bash
git reset HEAD your_file
```

### 消除最近的几次提交
```bash
git reset --hard HEAD~3
```

### 查看不同提交的指定文件差异
```bash
git diff 24587~ your_file
```

### 正确删除文件的方法
```bash
git rm your_file # 删除文件并提交
git commit -m "delete file"
```

### 开发中临时加塞了紧急任务怎么处理
```bash
git stash # 暂存工作区
# 开发紧急任务
git stash pop # 恢复工作区
```

### 指定不需要git管理的文件
```bash
echo your_file >> .gitignore
```

### 将 Git 仓库备份到本地
```bash
git clone your_repo local_repo
```

