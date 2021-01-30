from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.jobstreet.com.my/en/job-search/software-engineer-jobs/?ojs=10').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
job_title = article.div.div.div.div.h1.a.div.text
company =  article.div.div.div.span.text
time = article.div.div.div.time.text
#category = article.div.div.div.div.div.text
category = article.find('dd').text
location = article.find_all('span', class_='FYwKg _1GAuD C6ZIU_6 _1_nER_6 _27Shq_6 sQuda_6')

print(job_title)
print(company)
print(category)
print(time)
print(location[0].text)
print(location[1].text)

"""
Html sample job card
<article class="FYwKg _3j_fQ _2mOt7_6 _1A6vC_6 _4I9aG _58veS_6" data-automation="job-card-1">
    <div class="FYwKg _1A6vC_6 _31UWZ sXF6i _2cWXo _1Swh0">
        <img
            class="FYwKg _1GAuD _1quaz_6 _3CnZK_6"
            data-automation="job-card-banner"
            src="https://image-service-cdn.seek.com.au/9d309fdae3ac9d7ab4359e5ff8a00321b7e38882/a868bcb8fbb284f4e8301904535744d488ea93c1"
            alt="SEEK Asia (JobStreet)'s banner"
        />
        <div class="FYwKg _31UWZ _27u74_6">
            <div class="FYwKg _31UWZ fB92N_6 _1pAdR_6 FLByR_6 _2QIfI_6 _2cWXo _1Swh0 HdpOi">
                <div class="FYwKg">
                    <div class="FYwKg _36UVG_6" data-automation="job-card-logo">
                        <img class="FYwKg _1qfRc_6" src="https://image-service-cdn.seek.com.au/a1656dee9b728ef8aa7cbb8788326c2e08c8a8d0/ee4dce1061f3f616224767ad58cb2fc751b8d2dc" alt="SEEK Asia (JobStreet)'s logo" />
                    </div>
                    <div class="FYwKg _36UVG_6">
                        <h1 class="FYwKg _1GAuD C6ZIU_6 _6ufcS_6 _27Shq_6 sQuda_6">
                            <a
                                href="/en/job/software-engineer-4473421?jobId=jobstreet-my-job-4473421&amp;sectionRank=2&amp;token=0~ea1f8901-22b8-4d3f-b356-7298a4ce30c0&amp;fr=SRP%20View%20In%20New%20Tab"
                                target="_top"
                                rel="noopener noreferrer"
                                class="DvvsL_6 _1p9OP"
                            >
                                <div class="FYwKg _2j8fZ_6 sIMFL_6 _1JtWu_6">Software Engineer</div>
                            </a>
                        </h1>
                        <span class="FYwKg _1GAuD C6ZIU_6 _1_nER_6 _27Shq_6 _29m7__6">
                            <span class="FYwKg sXF6i _1GAuD _29LNX"><a href="/en/job-search/jobs-at-seek-asia-jobstreet/" class="_1p9OP" title="Show more jobs at SEEK Asia (JobStreet)">SEEK Asia (JobStreet)</a></span>
                        </span>
                    </div>
                    <span class="FYwKg _1GAuD C6ZIU_6 _1_nER_6 _27Shq_6 sQuda_6">
                        <span class="FYwKg sXF6i _1GAuD _29LNX"><a href="/en/job-search/software-engineer-jobs-in-kuala-lumpur/" class="_1p9OP" title="Limit results to Kuala Lumpur ">Kuala Lumpur</a></span>
                    </span>
                    <div class="FYwKg _1WMOl_6 _1GAuD" data-automation="job-card-selling-points">
                        <ul class="FYwKg _302h6 d7v3r _2uGS9_6">
                            <li class="FYwKg zoxBO_6">
                                <div class="FYwKg _2cWXo">
                                    <div class="FYwKg _1GAuD C6ZIU_6 _1_nER_6 _27Shq_6 _29m7__6 _1PM5y_6">
                                        <div class="FYwKg _2cWXo UAVGz _2Dyls _36CLf_6" aria-hidden="true"><div class="FYwKg _2YogD _25blN _2FgpS"></div></div>
                                    </div>
                                    <div class="FYwKg _20Cd9 _36Q-K _3RqUb_6"><span class="FYwKg _1GAuD C6ZIU_6 _1_nER_6 _27Shq_6 _29m7__6 _1PM5y_6">Genuine Work-life balance and flexible working hours</span></div>
                                </div>
                            </li>
                            <li class="FYwKg zoxBO_6">
                                <div class="FYwKg _2cWXo">
                                    <div class="FYwKg _1GAuD C6ZIU_6 _1_nER_6 _27Shq_6 _29m7__6 _1PM5y_6">
                                        <div class="FYwKg _2cWXo UAVGz _2Dyls _36CLf_6" aria-hidden="true"><div class="FYwKg _2YogD _25blN _2FgpS"></div></div>
                                    </div>
                                    <div class="FYwKg _20Cd9 _36Q-K _3RqUb_6"><span class="FYwKg _1GAuD C6ZIU_6 _1_nER_6 _27Shq_6 _29m7__6 _1PM5y_6">Transforming lives through customer-centric products &amp; technology</span></div>
                                </div>
                            </li>
                            <li class="FYwKg zoxBO_6">
                                <div class="FYwKg _2cWXo">
                                    <div class="FYwKg _1GAuD C6ZIU_6 _1_nER_6 _27Shq_6 _29m7__6 _1PM5y_6">
                                        <div class="FYwKg _2cWXo UAVGz _2Dyls _36CLf_6" aria-hidden="true"><div class="FYwKg _2YogD _25blN _2FgpS"></div></div>
                                    </div>
                                    <div class="FYwKg _20Cd9 _36Q-K _3RqUb_6"><span class="FYwKg _1GAuD C6ZIU_6 _1_nER_6 _27Shq_6 _29m7__6 _1PM5y_6">Work with us, and we’ll work with you on your career growth!</span></div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="FYwKg _3O7Hk_6 _2cWXo UAVGz HdpOi">
                    <time class="FYwKg _1GAuD" datetime="2021-01-29T12:46:58.000Z"><span class="FYwKg _1GAuD C6ZIU_6 _1_nER_6 u7OQ5_6 _29m7__6">19h ago</span></time>
                    <div class="FYwKg _3ra6Y _3hAhl_6">
                        <button class="FYwKg _2CaaD _2YogD _2UR0D_6 ZDQa2_6 _4I9aG _2cWXo UAVGz _1QYmq _1N44__6" aria-label="Toggle job shelf links" aria-expanded="false">
                            <span class="FYwKg _1GAuD C6ZIU_6 _1_nER_6 u7OQ5_6 _29m7__6 _1PM5y_6">
                                <svg viewBox="0 0 24 24" focusable="false" fill="currentColor" width="16" height="16" class="FYwKg _3VCZm _2Cp5K eO0my u7OQ5_6 _1HqaG _2ZfBL pgLNd" aria-hidden="true">
                                    <path d="M20.7 7.3c-.4-.4-1-.4-1.4 0L12 14.6 4.7 7.3c-.4-.4-1-.4-1.4 0s-.4 1 0 1.4l8 8c.2.2.5.3.7.3s.5-.1.7-.3l8-8c.4-.4.4-1 0-1.4z"></path>
                                </svg>
                            </span>
                        </button>
                    </div>
                </div>
            </div>
            <div class="FYwKg _3ra6Y _3hAhl_6">
                <div class="FYwKg _3TDN__6" aria-hidden="true">
                    <div class="FYwKg _6Gmbl_6 _3j1Zv_6 FLByR_6 _2QIfI_6 _2uf_M_6">
                        <dl class="FYwKg _1GAuD C6ZIU_6 _1_nER_6 u7OQ5_6 _29m7__6">
                            <dt class="FYwKg _1fD1J_6" style="color: #1c1c1c;"><strong class="sQuda_6">Job Specializations</strong></dt>
                            <dd class="FYwKg _2rhiT">
                                <a href="/en/job-search/software-engineer-jobs/?specialization=508" rel="nofollow" class="ELZOd_6 qbDva _2CELK_6 FYwKg _2k9O2 _4I9aG" title="Limit results to Computer/Information Technology ">
                                    Computer/Information Technology
                                </a>
                            </dd>
                            /
                            <dd class="FYwKg _2rhiT">
                                <a href="/en/job-search/software-engineer-jobs/?specialization=191" rel="nofollow" class="ELZOd_6 qbDva _2CELK_6 FYwKg _2k9O2 _4I9aG" title="Limit results to IT-Software in Computer/Information Technology">
                                    IT-Software
                                </a>
                            </dd>
                            <div class="FYwKg _6Gmbl_6 _3j1Zv_6">
                                <div class="FYwKg _3VCZm"><div class="FYwKg _20Cd9 _2_vLJ _1vY2t_6 TfmPI_6"></div></div>
                            </div>
                            <dt class="FYwKg _1fD1J_6" style="color: #1c1c1c;"><strong class="sQuda_6">Job Type</strong></dt>
                            <dd class="FYwKg _2rhiT">
                                <a href="/en/job-search/software-engineer-jobs/?job-type=full_time" rel="nofollow" class="ELZOd_6 qbDva _2CELK_6 FYwKg _2k9O2 _4I9aG" title="Limit results to Full-Time ">Full-Time</a>
                            </dd>
                        </dl>
                    </div>
                </div>
            </div>
        </div>
    </div>
</article>

"""

# salary = soup.find_all('span', class_='FYwKg sXF6i _1GAuD _29LNX')
# print(salary[0].text)
# print(salary[1].text)
# print(salary[2].text)
# print(salary[3].text)
# job = soup.find_all('div', class_='FYwKg _2j8fZ_6 sIMFL_6 _1JtWu_6')
# company = soup.find_all('div', class_='FYwKg _36UVG_6')
# salary = soup.find_all('span', class_='FYwKg _1GAuD C6ZIU_6 _1_nER_6 _27Shq_6 sQuda_6')
# i=0
# while i < len(salary):
#     print(salary[i].text)
#     i = i + 1

# i=0
# while i < len(company):
#     print(company[i].text)
#     i = i + 1
    
