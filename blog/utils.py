from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import cv2
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plb
import numpy as np
import io
from django.conf import settings
from django.views import generic
import collections
import base64
import json




         
def doRinkaku(name):
    org_file = settings.MEDIA_NAME + '/' + name
    result1_file = settings.MEDIA_NAME + '/ss_' + name
    result2_file = result1_file.replace('.jpg', '.png').replace('.jpeg', '.png')
    # original（輪郭記述用）
    img_org = cv2.imread(org_file)

    # グレースケール化
    img_tmp = cv2.cvtColor(img_org, cv2.COLOR_BGR2GRAY)
    
    # 2値化
    ret, img_tmp = cv2.threshold(img_tmp,250, 256, cv2.THRESH_BINARY_INV) # 2値化type
    cv2.imwrite(settings.MEDIA_NAME + '/tmp_' + name, img_tmp)
    #ret, img_tmp = cv2.threshold(img_tmp, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #img_tmp = cv2.adaptiveThreshold(img_tmp, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 3)

    # 黒塗り画像作成
    ret, img_tmp2 = cv2.threshold(img_tmp,255,256,cv2.THRESH_BINARY) 

    # 境界線探索
    # - 第2引数:
    #   - cv2.RETR_EXTERNAL は最外周のみ探索
    #   - cv2.RETR_TREE     は全境界(輪郭? 等高線?)を探索
    # - 返り値:
    #   - contours : 探索された境界
    #   - hierarchy: 境界が複数ある場合の階層
    contours, hierarchy = cv2.findContours(img_tmp,
                                                cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_SIMPLE )

    contours.sort(key=cv2.contourArea, reverse=True)
    i  = 0
    for contour in contours:
        arclen = cv2.arcLength(contour,
                               True) # 対象領域が閉曲線の場合、True
        approx = cv2.approxPolyDP(contour,
                                  0.005*arclen,  # 近似の具合?
                                  True)
        # 境界の描画 
        cv2.drawContours(img_org,
                         [approx],
                         -1,    # 表示する輪郭. 全表示は-1
                         (255,255, 0),
                         2)    # 等高線の太さ
                         
        # 境界の描画 ( 黒塗り画像の中に白い輪郭描画 )
        cv2.drawContours(img_tmp2,
                         [approx],
                         -1,    # 表示する輪郭. 全表示は-1
                         (255,255, 255),
                         -1)    # 等高線の太さ
       
        i += 1
        if i > 0:
            break
    cv2.imwrite(result1_file, img_org)
    #cv2.imwrite(settings.DOC_DIR + 'img_org2.jpg', img_org2)
    # 背景透過処理
    result_img = cv2.merge(cv2.split(cv2.imread(org_file)) + [img_tmp2])
    cv2.imwrite(result2_file, result_img)
