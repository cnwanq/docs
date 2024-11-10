# React Router

## 什么是路由
1. 多页面
2. 单页面

如何区别是多页面还是单页面？
切换页面，浏览器刷新按钮是否状态改变。
多页面，是存在多个不同的html页面，通过window.location互相跳转。每个页面都需要重新加载资源，SEO友好。
单页面，只有一个html页面，通过局部刷新的原理，利用JS控制页面。页面跳转，不要刷新，性能和体验会比较好。


## 安装react-router
```
pnpm install react-router-dom
```

react-router 与 react-router-dom 的区别
react-router-dom 内部依赖 react-router。在浏览器里开发。
react-router-native 针对的是移动端 react-native。

## 路由模式
* BrowserRouter
* HashRouter
* MemoryRouter
* NativeRouter
* StaticRouter

依赖包是 `react-router-dom`

### BrowserRouter
```tsx
<BrowserRouter>
    <Routes>
        <Route path="/" element={<App />} />
    </Routes>
</BrowserRouter>
```

### HashRouter
```tsx
<HashRouter>
    <Routes>
        <Route path="/" element={<App />} />
    </Routes>
</HashRouter>
```

### MemoryRouter
```tsx
<MemoryRouter>
    <Routes>
        <Route path="/" element={<App />} />
    </Routes>
</MemoryRouter>
```

### NativeRouter
ReactNative 使用的

### StaticRouter
Node 环境服务端渲染使用的

### 在路由中进场使用的标签
```
BrowserRouter
Routes
Route
Outlet
```

## 动态路由
```

```

## 数据路由
传统路由解决的是路由与UI之间的关系

应用初始化 -> 路由切换、加载页面 -> 页面生命周期、组件挂载、更新数据 -> 页面渲染展示

数据路由解决的是路由与UI和数据之间的关系

应用初始化 -> 路由切换、加载页面 ｜ 加载数据 ｜ 分包加载 -> 页面渲染展示

```
<RouterProvider>
```



## 一些API
* useLocation
  获取当前的浏览器 location 对象
* useParams
  获取当前路由的 params 对象
* useSearchParams
  获取路由链接的参数 searchParams 对象
* useMatch
  匹配当前页面链接是否匹配
  
