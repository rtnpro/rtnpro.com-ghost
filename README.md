# Description

This is content data for the Ghost blog running at www.rtnpro.com.


# Setup

This will run you through how to setup this blog using a Docker container
running behind Nginx, and with SELinux enabled on CentOS 7.

```
git clone https://github.com/rtnpro/rtnpro.com
cd rtnpro.com

# Allow sharing this directory with a Docker container
sudo chcon -Rt svirt_sandbox_file_t ./

# Allow nginx access port 2368 expose from Docker container
sudo semanage port -a -t http_port_t -p tcp 2368

# Run container
sudo docker run -d -ti -p 2368:2368 --name rtnpro_com_ghost -v $(pwd):/var/lib/ghost -v $(pwd)/themes:/usr/src/ghost/content/themes -e NODE_ENV=production ptimof/ghost

cp nginx.conf /etc/nginx/conf.d/www.rtnpro.com.conf

sudo service nginx restart
```
