from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.core.paginator import Paginator
from django.db.models import Q
import logging


logger = logging.getLogger('pybo')

# Create your views here.
def index(request):
    #3/0
    logger.info("INFO 레벨로 출력")
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '')  # 검색어
    #작성일자 역순으로 조회 리스트 저장
    question_list = Question.objects.order_by('-create_date')
    
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
        
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    #context = {'question_list':question_list}
    context = {'question_list':page_obj, 'test_var':'test11', 'page': page, 'kw': kw}
    #return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다. 11")
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html',context)
