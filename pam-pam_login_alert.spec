%define 	modulename pam_login_alert
Summary:	A module that informs admin about logins into system
Summary(pl.UTF-8):   Moduł informujący administratora o logowaniu do systemu
Name:		pam-%{modulename}
Version:	0.10
Release:	3
Epoch:		0
License:	GPL
Vendor:		Dustin Puryear <dpuryear@usa.net>
Group:		Applications/System
Source0:	http://www.kernel.org/pub/linux/libs/pam/pre/modules/%{modulename}-%{version}.tar.bz2
# Source0-md5:	55591c36291247977fd7e1e824191f05
URL:		http://www.kernel.org/pub/linux/libs/pam/pre/modules/
BuildRequires:	pam-devel
BuildRequires:	sed >= 4
Obsoletes:	pam_login_alert
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alert an administrator via email and/or syslog when a given user(s)
accesses the system. Useful primarily when monitoring user activity
and access.

%description -l pl.UTF-8
Moduł informujący administratora pocztą elektroniczną lub przez
sysloga o logowaniu do systemu wybranych użytkowników. Przydatny
podczas śledzenia aktywności użytkowników.

%prep
%setup -q -c -n %{modulename}-%{version}
# corrects paths
sed -i 's,/etc/login_alert.users,/etc/security/login_alert.users,' *
sed -i 's,/etc/login_alert.conf,/etc/security/login_alert.conf,' *

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -Wall" \
	LD="%{__cc}" \
	LDFLAGS="%{rpmldflags} -shared -lpam"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/security,/%{_lib}/security} \
	   $RPM_BUILD_ROOT%{_mandir}/man8

install pam_login_alert.so $RPM_BUILD_ROOT/%{_lib}/security
install login_alert.conf $RPM_BUILD_ROOT/etc/security/login_alert.conf
install login_alert.users $RPM_BUILD_ROOT/etc/security/login_alert.users
install pam_login_alert.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) /%{_lib}/security/pam_login_alert.so
%{_mandir}/man8/*
%config(noreplace) %verify(not md5 mtime size) /etc/security/login_alert.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/login_alert.users
