# React 学习笔记

*React 和 ReactDom 的区别，为什么有俩个库？*
react: 这是React库的核心。它定义了React组件的创建和生命周期的方法，以及React元素的概念。你可以将其视为React的引擎。

react-dom: 这个库提供了在浏览器环境中使用React的方法，例如将React组件渲染到DOM中。它是React的一部分，用于处理与浏览器相关的操作。你可以将其视为React的驱动程序。

*React 严格模式的作用*
React 严格模式的作用是在开发过程中提供额外的检查和警告，以帮助你发现潜在的问题和错误。它可以帮助你在开发过程中捕获一些常见的错误，例如意外的副作用、不安全的生命周期方法等。

*JSX 的作用*
JSX 是一种用于在 JavaScript 中编写 HTML 代码的语法扩展。它允许你在 JavaScript 代码中嵌入 HTML 标签，使代码更加清晰易读。JSX 最终会被编译成 JavaScript 代码，以便在浏览器中运行。 


*React 组件*
* 创建组件有两种方式
    1. 类组件
    2. 函数组件
* 类组件
    1. 必须继承 React.Component
    2. 必须实现 render 方法
    3. 必须使用大写字母开头
    4. 可以使用 state 和 props
    5. 可以使用生命周期方法
    6. 可以使用 this 关键字
    7. 可以使用 setState 方法
* 函数组件
    1. 必须使用小写字母开头
    2. 必须返回 JSX
    3. 可以使用 props
    4. 可以使用 useState 钩子
    5. 可以使用 useRef 钩子
    6. 可以使用 useContext 钩子
    7. 可以使用 useReducer 钩子

*React 类组件生命周期*
React类组件生命周期分为三个阶段：
1. 挂载阶段（Mounting）：组件被创建并插入到DOM中。
2. 更新阶段（Updating）：组件的状态或属性发生变化时触发。
3. 卸载阶段（Unmounting）：组件从DOM中移除。

* React 类组件生命周期方法
** 挂载阶段（Mounting）**
1. constructor：组件构造函数，用于初始化组件的状态和绑定事件处理函数。
2. render：渲染组件的内容，返回一个React元素。
3. componentDidMount：组件挂载到DOM后执行，通常用于发送网络请求或订阅事件。

** 更新阶段（Updating）**
1. render：重新渲染组件的内容，返回一个React元素。
2. componentDidUpdate：组件更新后执行，通常用于更新DOM或发送网络请求。

** 卸载阶段（Unmounting）**
1. componentWillUnmount：组件即将从DOM中移除时执行，通常用于清理定时器、取消订阅事件等。
2. componentDidUnmount：组件从DOM中移除后执行，通常用于清理组件的资源。



** React早期的生命周期方法 **
1. constructor：组件构造函数，用于初始化组件的状态和绑定事件处理函数。
2. componentWillReceiveProps：组件接收到新的props时执行，通常用于更新组件的状态。
3. shouldComponentUpdate：组件是否应该更新，返回一个布尔值。
4. componentWillUpdate：组件即将更新时执行，通常用于更新组件的状态。
5. componentDidUpdate：组件更新后执行，通常用于更新DOM或发送网络请求。
6. componentWillUnmount：组件即将从DOM中移除时执行，通常用于清理定时器、取消订阅事件等。

** React16 的生命周期方法**
1. constructor：组件构造函数，用于初始化组件的状态和绑定事件处理函数。
2. getDerivedStateFromProps：组件接收到新的props时执行，返回一个对象用于更新组件的状态。
3. render：渲染组件的内容，返回一个React元素。
4. componentDidMount：组件挂载到DOM后执行，通常用于发送网络请求或订阅事件。
5. shouldComponentUpdate：组件是否应该更新，返回一个布尔值。
6. getSnapshotBeforeUpdate：组件即将更新时执行，返回一个值用于更新DOM。
7. componentDidUpdate：组件更新后执行，通常用于更新DOM或发送网络请求。
8. componentWillUnmount：组件即将从DOM中移除时执行，通常用于清理定时器、取消订阅事件等。

