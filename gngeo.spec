Summary:	A good Neo-Geo emulator
Summary(de.UTF-8):	Ein guter Neo-Geo Emulator
Summary(pl.UTF-8):	Dobry emulator Neo-Geo
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
BuildRequires:	autoconf
BuildRequires:	automake
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gngeo is a program that emulates the SNK Neo-Geo game system. It uses
SDL and optimized assembly CPU emulation cores on i386 platforms.

%description -l de.UTF-8
gngeo ist ein Programm dass das SNK Neo-Geo Spielsystem emuliert. Es
benutzt SDL und eine in Assembler optimisierte CPU Emulation für i386
Architekturen.

%description -l pl.UTF-8
gngeo to program emulujący system gier SNK Neo-Geo. Wykorzystuje SDL i
zoptymalizowaną w asemblerze emulację CPU na platformach i386.

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
