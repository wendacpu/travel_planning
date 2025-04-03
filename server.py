#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简单的HTTP服务器，用于提供旅行规划HTML页面
"""

import http.server
import socketserver
import os

# 定义端口
PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 如果访问根目录，展示项目介绍
        if self.path == '/':
            self.path = '/index.html'
            
            # 检查index.html是否存在，不存在则创建
            if not os.path.exists('index.html'):
                with open('index.html', 'w', encoding='utf-8') as f:
                    f.write('''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>旅行规划指南</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="mb-4">高德地图旅行规划指南</h1>
        
        <div class="row">
            <div class="col-md-4 mb-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">武汉一日游</h5>
                        <p class="card-text">探索武汉市区的精华景点，包含黄鹤楼、户部巷、东湖等著名景点。</p>
                        <a href="wuhan_guide.html" class="btn btn-primary">查看指南</a>
                    </div>
                </div>
            </div>
            
            <div class="col-md-4 mb-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">武汉大学一日游</h5>
                        <p class="card-text">武大樱花季特别版，游览珞珈山校园、樱花大道、凌波门等地标。</p>
                        <a href="whu_guide.html" class="btn btn-primary">查看指南</a>
                    </div>
                </div>
            </div>
            
            <div class="col-md-4 mb-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">云南旅行指南</h5>
                        <p class="card-text">云南特色景点介绍，包含大理、丽江、昆明等热门旅游目的地。</p>
                        <a href="yunnan_guide.html" class="btn btn-primary">查看指南</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>''')
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def run_server():
    # 创建HTTP服务器
    handler = MyHttpRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"服务器启动在端口 {PORT}")
        print(f"请访问: http://localhost:{PORT}/")
        print("按Ctrl+C停止服务器")
        
        # 保持服务器运行
        httpd.serve_forever()

if __name__ == "__main__":
    run_server() 