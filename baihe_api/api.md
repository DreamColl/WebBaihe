# API Doc

## Auth

### 获取token

**POST /token/**

Permission: **none**

#### Parameters:

| Field    | Type   | Description |
| -------- | ------ | ----------- |
| username | string | username    |
| password | string | password    |

#### Response


```json
{
  "token": "d541cb93754ffe006a38e97519780ce02be52f58"
}
```



## Articals

### 获取文章列表

**GET /api/articals/**

Permission: **none**

#### Paramaters

| Field | Type | Description                          |
| ----- | ---- | ------------------------------------ |
| page  | int  | optional, page number default page=1 |

#### Response

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "url": "http://127.0.0.1:8000/api/articals/2/",
      "author": "shady",
      "author_detail": "http://127.0.0.1:8000/api/users/2/",
      "title": "标题1",
      "content": "正文正文正文",
      "read_count": 0,
      "share_count": 0,
      "created": "2017-01-15T14:09:42.630213Z"
    },
    {
      "url": "http://127.0.0.1:8000/api/articals/3/",
      "author": "shady",
      "author_detail": "http://127.0.0.1:8000/api/users/3/",
      "title": "标题2",
      "content": "正文正文正文222132",
      "read_count": 0,
      "share_count": 0,
      "created": "2017-01-15T14:10:06.716557Z"
    }
  ]
}
```

###  新建文章

**POST /api/articals/**

Permission: **staff**

#### Paramaters

| Field   | Type   | Description       |
| ------- | ------ | ----------------- |
| title   | string | 必填，文章标题，最大长度128个字 |
| content | string | 必填，正文内容           |

#### Response

```json
{
  "url": "http://127.0.0.1:8000/api/articals/4/",
  "author": "shady",
  "author_detail": "http://127.0.0.1:8000/api/users/4/",
  "title": "标题1",
  "content": "正文正文正文",
  "read_count": 0,
  "share_count": 0,
  "created": "2017-01-15T14:51:28.947841Z"
}
```

### 获取文章详情

**GET /api/articals/:id/**

Permission: **none**

#### Paramaters

| Fields | Type | Description |
| ------ | ---- | ----------- |
| id     | int  | 文章id        |

#### Response

```json
{
  "url": "http://127.0.0.1:8000/api/articals/4/",
  "author": "shady",
  "author_detail": "http://127.0.0.1:8000/api/users/4/",
  "title": "标题1",
  "content": "正文正文正文",
  "read_count": 0,
  "share_count": 0,
  "created": "2017-01-15T14:51:28.947841Z"
}
```

### 删改文章

**DELETE|PUT|PATCH /api/articals/:id/**

参数参考增查



## User

略



## 表单

### 获取表单列表

**GET /api/form/**

Permission: **none**

#### Paramaters

| Field | Type | Description                          |
| ----- | ---- | ------------------------------------ |
| page  | int  | optional, page number default page=1 |

#### Response

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "url": "http://127.0.0.1:8000/api/form/1/",
      "name": "表单1",
      "comment": null,
      "structure": "",
      "created": "2017-01-15T15:54:01.726573Z",
      "start_time": "2017-01-20T00:00:00Z",
      "end_time": "2017-01-20T01:00:00Z"
    },
    {
      "url": "http://127.0.0.1:8000/api/form/2/",
      "name": "表单2",
      "comment": null,
      "structure": "",
      "created": "2017-01-15T15:54:41.929614Z",
      "start_time": "2017-01-20T00:00:00Z",
      "end_time": "2017-01-20T01:00:00Z"
    }
  ]
}
```

### 创建表单

**POST /api/form/**

Permission: **staff**

#### Paramaters

| Field      | Type                                     | Description        |
| ---------- | ---------------------------------------- | ------------------ |
| name       | string                                   | 必填，表单名，长度不超过       |
| start_time | datetime (YYYY-MM-DD hh:mm\[:ss\[.uuuuuu\]\]\[+HH:MM\|-HH:MM\|Z\]) | 必填，表单起始时间，必须大于现在   |
| end_time   | datetime (YYYY-MM-DD hh:mm\[:ss\[.uuuuuu\]\]\[+HH:MM\|-HH:MM\|Z\]) | 必填，表单结束时间，必须大于开始时间 |
| structure  | json                                     | 必填，具体结构还没定         |
| comment    | string                                   | 选填，表单备注            |

#### Response

```json
{
  "url": "http://127.0.0.1:8000/api/form/2/",
  "name": "表单2",
  "comment": null,
  "structure": "",
  "created": "2017-01-15T15:54:41.929614Z",
  "start_time": "2017-01-20T00:00:00Z",
  "end_time": "2017-01-20T01:00:00Z"
}
```

### 获取表单详情

**GET /api/form/:id/**

Permission: **none**

#### Paramaters

| Fields | Type | Description |
| ------ | ---- | ----------- |
| id     | int  | 表单id        |

#### Response

```json
{
  "url": "http://127.0.0.1:8000/api/form/2/",
  "name": "表单2",
  "comment": null,
  "structure": "",
  "created": "2017-01-15T15:54:41.929614Z",
  "start_time": "2017-01-20T00:00:00Z",
  "end_time": "2017-01-20T01:00:00Z"
}
```

### 删改表单

**DELETE|PUT|PATCH /api/form/:id/**

参数参考增查