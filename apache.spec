Summary:     HTTP server daemon to provide WWW services
Summary(de): Leading World Wide Web-Server
Summary(fr): Serveur Web leader du marché
Summary(pl): Serwer WWW (World Wide Web)
Summary(tr): Lider WWW tarayýcý
Name:        apache
Version:     1.3.3
Release:     1
Group:       Networking/Daemons
Source0:     ftp://ftp.apache.org/apache/dist/%{name}_%{version}.tar.gz
Source1:     httpd.init
Source2:     apache.log
Patch0:      apache-suexec.patch
Patch1:      apache-config.patch
Copyright:   BSD-like
Obsoletes:   apache-extra
Provides:    httpd
Requires:    /etc/mime.types, initscripts >= 3.25, setup >= 1.10.0
Prereq:      /sbin/chkconfig
URL:         http://www.apache.org/
BuildRoot:   /tmp/%{name}-%{version}-root

%description
Apache is a full featured web server that is freely available, and also
happens to be the most widely used.

%description -l de
Apache ist ein voll funktionsfähiger Web-Server, der kostenlos
erhältlich und weit verbreitet ist.

%description -l fr
Apache est un serveur Web complet, disponible librement, et se trouve être
aussi le plus utilisé à travers le monde.

%description -l pl
Apache jest serwerem WWW (World Wide Web). Instaluj±c ten
pakiet bêdziesz móg³ prezentowaæ w³asne strony WWW w sieci internet
Apache umozliwia równie¿ konfigurowanie serwerów wirtualnych.

%description -l tr
Apache serbest daðýtýlan ve çok kullanýlan yetenekli bir web sunucusudur.

%package suexec
Summary:     Apache suexec wrapper
Summary(pl): suexec wrapper do serwera www Apache
Group:       Networking/Daemons
Requires:    %{name} = %{version}

%description suexec
The suEXEC feature provides Apache users the ability to run CGI and SSI
programs under user IDs different from the user ID of the calling web-server.
Normally, when a CGI or SSI program executes, it runs as the same user 
who is running the web server. 

%description -l pl suexec
suEXEC umo¿liwia serwerowi Apache uruchamianie programów CGI i SSI z innym
UID ni¿ wywo³yj±cy je serwer. Normalnie programy CGI i SSI s± wykonywane
jako taki sam urzytkownik jak serwer WWW.

%package devel
Summary:     Apache include files
Summary(pl): Pliki nag³ówkowe do serwera www Apache
Group:       Networking/Development
Requires:    %{name} = %{version}

%description devel
Apache include files.

%description -l pl devel
Pliki nag³owkowe do serwera www Apache.

%package doc
Summary:     Apache dokumentation
Summary(pl): Dokumentacja do Apache
Group:       Documentation
Requires:    %{name} = %{version}

%description doc
Documentation for apache in HTML format.

%description -l pl doc
Dokumentacja do Apache w formacie HTML

%prep 
%setup -q -n apache_%{version}
%patch0 -p1
%patch1 -p1

%build
OPTIM="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr \
	--sysconfdir=/etc/httpd/conf \
	--datadir=/home/httpd \
	--libexecdir=/usr/libexec/apache \
	--localstatedir=/var \
	--runtimedir=/var/run \
	--logfiledir=/var/log/httpd \
	--without-confadjust \
	--enable-module=all \
	--enable-shared=max \
	--proxycachedir=/var/spool/proxy \
	--with-perl=/usr/bin/perl \
	--enable-suexec \
	--suexec-caller=http \
	--suexec-uidmin=500 \
	--suexec-gidmin=500

make

%install
rm -rf $RPM_BUILD_ROOT
make install-quiet root="$RPM_BUILD_ROOT"

install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d}

install $RPM_SOURCE_DIR/apache.log $RPM_BUILD_ROOT/etc/logrotate.d/apache
install $RPM_SOURCE_DIR/httpd.init $RPM_BUILD_ROOT/etc/rc.d/init.d/httpd

# Only needed for from_cvs tarballs, but doesn't hurt otherwise
rm -f $RPM_BUILD_ROOT/home/httpd/html/manual/expand.pl

strip --strip-debug $RPM_BUILD_ROOT/usr/libexec/apache/*.so || :

touch $RPM_BUILD_ROOT/var/log/httpd/{access,error,suexec}_log

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add httpd

%preun
if [ $1 = 0 ]; then
   if [ -f /var/lock/subsys/httpd ]; then
       /etc/rc.d/init.d/httpd stop
   fi
   /sbin/chkconfig --del httpd
fi

%files
%defattr(644, root, root, 755)
%doc ABOUT_APACHE src/CHANGES KEYS LICENSE README
%doc src/support/suexec.[ch]
%doc /home/httpd/html/manual

%dir /etc/httpd
%dir /etc/httpd/conf
%config(noreplace) %verify(not size mtime md5) /etc/httpd/conf/*.conf
/etc/httpd/conf/*.conf.default
%attr(600, root, root) %config /etc/logrotate.d/*
%attr(755, root, root) %dir /home/httpd
%attr(755, root, root) %dir /home/httpd/html
%config(noreplace) /home/httpd/html/index.html
/home/httpd/html/apache_pb.gif
%attr(755, root, root) /etc/rc.d/init.d/httpd
%attr(755, root, root, 755) /home/httpd/cgi-bin
%attr(755, root, root, 755) /usr/libexec/apache
%dir /home/httpd/icons
/home/httpd/icons/*.gif
%attr(755, root, root) /usr/bin/*
%attr(755, root, root) /usr/sbin/ab
%attr(755, root, root) /usr/sbin/apachectl
%attr(755, root, root) /usr/sbin/apxs
%attr(755, root, root) /usr/sbin/httpd
%attr(755, root, root) /usr/sbin/logresolve
%attr(755, root, root) /usr/sbin/rotatelogs
%attr(4751,root, root) /usr/sbin/suexec
%attr(644, root,  man) /usr/man/man[18]/*
%attr(700, root, root) %dir /var/log/httpd
%ghost /var/log/httpd/*

%files suexec
%attr(4751,root, root) /usr/sbin/suexec
%ghost /var/log/httpd/suexec_log

%files devel
%attr(644, root, root, 755) /usr/include/apache

%files doc
%doc /home/httpd/html/manual

%changelog
* Wed Nov 13 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3.3-1]
- removed making symlinks in /etc/rc.d/rc?.d and in %install also
  removed this symlinks from %files (/etc/rc.d/init.d/httpd suports
  chkconfig),
- more simplifications in %install,
- added new apache-config.patch,
- added "%ghost /var/log/httpd/suexec_log" for suexec subpackage,
- added "Requires: setup >= 1.10.0" for proper install in enviroment with
  http user/group.

* Wed Oct 14 1998 Konrad Stêpieñ <konrad@interdata.com.pl>
  [1.3.3-0]
- changed user/group to http,
- enabled all modules,
- added magic (for mod_mime_magic),
- rebuild spec file to minimize number of patches,
- suEXEC in separated package.

* Fri Sep 25 1998 Konrad Stêpieñ <konrad@interdata.com.pl>
  [1.3.2-1]
- reconfig to use /etc/mime.types (again),
  orginal mime.types can be found in documentation directory
- restore orginal start page,
- added "Provides: httpd".

* Thu Sep  3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3.1-2]
- removed /home/httpd/icons/README
- added devel subpackage,
- added pl translation (Wojtek ¦lusarczyk <wojtek@shadow.eu.org>),
- removed Serial: filed,
- removed Packager: field (this must be placed in private ~/.rpmrc),
- simplification in %files and %install,
- /home/httpd/html/manual is now marked as %doc,
- added /etc/rc.d/rc*.d/* symlinks as a %config(missingok),
- changed permidssion on logrotate config file to 600,
- changed permidssion on /var/log/httpd to 700,
- added %ghost /var/log/httpd/*
- added striping modules.
- added patch to defeat header dos attack

* Sat Jul 18 1998 Manoj Kasichainula <manojk@io.com>
  [1.3.1-1]
some of the changes from 1.3.0-1 (mine was done independantly, so there are
probably other changes)
- /etc/rc.d/init.d/httpd includes reload
- logrotate doesn't kill all httpd processes, just one. This is recommended.
- Doesn't uses Red Hat MIME typesm since RH mime.types doesn't include .htm,
  and there are other differences which will probably just cause lots of
  annoying bug reports
- Don't change ServerAdmin (this fake address is on purpose according
  to the Apache Group)
- don't enable mod_auth_dbm, since it can supposedly conflict with
  mod_auth_db

* Sun May 31 1998 Manoj Kasichainula <manojk@io.com>
  [1.3b8_dev-1]
- Updated to 1.3b8_dev
- Deleted some patchwork because of improvements in APACI
- Added translations from RH 5.1 Apache RPM
- Loosened permissions to match RH 5.1 Apache RPM in /home
- Allow index.htm
- Collapsed doc package into main package (partly inspired by RPM bug)

* Fri May 22 1998 Manoj Kasichainula <manojk@io.com>
  [1.3b7-0]
- Upgraded to 1.3b7
- Uses APACI configuration interface -- radical rewrite
- No more apache-extra, at least for now
- more descriptive Copyright field
- Now builds suEXEC
- Explicitly decided not to use built-in mime.types, but included patch to do
  so

* Thu Apr 16 1998 Manoj Kasichainula <manojk@io.com>
  [1.3b6-4]
- Upgraded to 1.3b6
- Split perl path patch from other config (saves a little time when upgrading
  packages)
- Started the process of separating out shared modules. So far, only the proxy
  module has been done.
- Yeah, I'm aware of 1.3b6-3 RPM in contrib. It has problems that I would
  discuss with the packager if I could find out who that was.

* Thu Mar 5 1998 Manoj Kasichainula <manojk@io.com>

- Upgraded to 1.3b5
- Buildable by non-root

* Fri Jan 2 1998 Manoj Kasichainula <manojk@io.com>

- Includes changes from Red Hat 5.0's Apache release
  - added patch for backslash DoS attach
  - made the default index.html be config(noreplace) so we no longer
    blow away other folks' index.html
  - added chkconfig support
  - added restart|status options to initscript
  - renamed httpd.init to httpd
  - New index.html
  - Now uses Red Hat's mime.types file (I may change my mind on this)
  - No longer keeps an agent and referer log.
  - Much more
- Upgraded to 1.3b3
- Fixed sillyness in /etc/rc.d/init.d/httpd
- Now require recent version of initscripts with killproc fix.
- Changed logrotate script
- Undid Red Hat's ServerAdmin change (Red Hat's choice results in a
  seemingly valid but nonsensical address)
- suexec moved to /home/httpd/sbin/suexec
- Replaced a reference to apache_pb.gif to /icons/apache_pb.gif, to save a
  bit of space)

* Thu Oct 16 1997 Manoj Kasichainula <manojk@io.com>
- Upgraded to 1.3b2
- MaxRequestsPerChild upped to 10000
- apache-suexec absorbed into apache
- Uncommented Serial: line. Now, it requires a recent version of RPM
