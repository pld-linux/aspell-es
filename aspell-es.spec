Summary:	Spanish dictionary for aspell
Summary(pl):	Hiszpa�ski s�ownik dla aspella
Name:		aspell-es
Version:	0.0
%define	subv	3
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	http://aspell.sourceforge.net/%{name}-%{version}-%{subv}.tar.bz2
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell
BuildRequires:	pspell-devel
Requires:	aspell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spanish dictionary (i.e. word list) for aspell.

%description -l pl
Hiszpa�ski s�ownik (lista s��w) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
%{_datadir}/pspell/*