# 路由

| path                | 文件                             | 功能      | 组件名          | 路由级别 |
| ------------------- | -------------------------------- | --------- | --------------- | -------- |
| /login              | views/login/LoginPage.vue        | 登录&注册 | LoginPage       | 一级路由 |
| /                   | views/layout/LayoutContainer.vue | 布局架子  | LayoutContainer | 一级路由 |
| ├─ /article/manage  | views/article/ArticleManage.vue  | 文章管理  | ArticleManage   | 二级路由 |
| ├─ /article/channel | views/article/ArticleChannel.vue | 频道管理  | ArticleChannel  | 二级路由 |
| ├─ /user/profile    | views/user/UserProfile.vue       | 个人详情  | UserProfile     | 二级路由 |
| ├─ /user/avatar     | views/user/UserAvatar.vue        | 更换头像  | UserAvatar      | 二级路由 |
| ├─ /user/password   | views/user/UserPassword.vue      | 重置密码  | UserPassword    | 二级路由 |

