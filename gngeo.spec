#
# TODO: pl,de translation
Summary:	A good Neo-Geo emulator
Name:		gngeo
Version:	0.6.12
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://m.peponas.free.fr/gngeo/download/%{name}-%{version}.tar.gz
# Source0-md5:	cad0232606b7c4f0449445ba0dea080f
Patch0:		%{name}-ac_patch.patch
URL:		http://m.peponas.free.pr/gngeo/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gngeo is a program that emulates the SNK Neo-Geo game system. It uses
SDL and optimized assembly CPU emulation cores on i386 platforms.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/gngeo*
